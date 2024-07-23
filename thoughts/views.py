from django.shortcuts import render, redirect
from .models import Thought
from .forms import ThoughtForm
from django.contrib import messages

def thoughts(request):
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    thoughts = Thought.objects.all()
    
    if request.method == 'POST':
        thought_input = request.POST.get('thought_input')
        form = ThoughtForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.author = profile
            thought.content = thought_input
            thought.save()
            messages.success(request, 'Thought added successfully!')
            return redirect('thoughts')
        
    context = {'profile':profile, 'thoughts':thoughts}
    return render(request, 'thoughts/thoughts.html', context)
