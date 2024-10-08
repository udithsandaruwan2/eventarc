from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Profile, Skill, Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MailForm
from django.db.models import Q
from .utils import searchProfiles, paginateProfiles

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'User login successfully!')
            return redirect('analytics')
            
        else:
            messages.error(request, 'Username or password is incorrect!')

    return render(request, 'users/login-register.html')

@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('thoughts')
        
        else:
            messages.error(request, 'An error has occurred during registation!')

    context = {'page':page, 'form':form}
    return render(request, 'users/login-register.html', context)

@login_required(login_url="login")
def profiles(request):
    page = "developers"
    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 9)
    context = {'profiles': profiles, 'search_query':search_query, 'custom_range':custom_range, 'page':page}
    return render(request, 'users/profiles.html', context)


@login_required(login_url="login")
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topskills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")

    context = {'profile':profile, 'topskills':topskills, 'otherskills':otherskills}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url="login")
def userAnalytics(request):
    page = "analytics"
    profile = request.user.profile
    
    context = {'profile':profile, 'page':page}
    return render(request, 'users/analytics.html', context)

@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile
    skill = profile.skill_set.all()

    topskills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")
        
    context = {'profile': profile, 'topskills': topskills, 'otherskills': otherskills}
    return render(request, 'users/account.html', context)

@login_required(login_url="login")
def updateProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form':form}
    return render(request, 'users/update-profile.html', context)

@login_required(login_url="login")
def addSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            return redirect('account')

    context = {'form':form}
    return render(request, 'users/add-skill.html', context)


@login_required(login_url="login")
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form':form}
    return render(request, 'users/update-skill.html', context)

@login_required(login_url="login")
def deleteSkill(request, pk):
    skill = Skill.objects.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('account')
    context = {'skill':skill}
    return render(request, 'users/delete-skill.html', context)


@login_required(login_url="login")
def inbox(request):
    page = "inbox"
    profile = request.user.profile
    message_request = profile.messages.all()
    unread_count = message_request.filter(is_read=False).count() 

    form = MailForm()

    if request.method == 'POST':
        form = MailForm(request.POST)
        
        if form.is_valid():
            mail = form.save(commit=False)
            mail.sender = profile
  
            # Handle file attachment if provided
            # if 'attach' in request.FILES:
                # mail.attach = request.FILES['attach']  # Assuming 'attach' is a file field   
            mail.save()
            # form.save()
            messages.success(request, 'Email sent successfully!')
            return redirect('inbox')
        else:
            messages.error(request, 'There was an error in the form. Please correct it and try again.')

    context = {'page': page, 'profile': profile, 'message_request': message_request, 'unread_count': unread_count, 'form':form}
    return render(request, 'users/inbox.html', context)


@login_required(login_url="login")
def mailPreview(request, pk):
    page = "mail-preview"
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    
    if message.is_read == False:
        message.is_read = True
        message.save()
        
    context = {'page':page, 'message':message}
    return render(request, 'users/mail-preview.html', context)