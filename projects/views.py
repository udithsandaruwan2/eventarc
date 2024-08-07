from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from .utils import searchProjects, paginateProjects


@login_required(login_url="login")
def projects(request):
    page = "projects"
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)
    context = {'projects':projects, 'search_query':search_query, 'custom_range': custom_range, 'page':page}
    return render(request, 'projects/projects.html', context)

@login_required(login_url="login")
def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {'project':project, 'tags':tags}
    return render(request, 'projects/single-project.html', context)

@login_required(login_url="login")
def createProject(request):
    page= "add-project"
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {'form':form, 'page':page}
    return render(request, 'projects/project-form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/project-form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'project':project}
    return render(request, 'projects/delete-obj.html', context)
