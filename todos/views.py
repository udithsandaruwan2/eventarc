from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def todoList(request):
    page = 'todos'
    profile = request.user.profile
    
    todos = Todo.objects.filter(owner=profile)
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_note = request.POST['todo_note']
            todo_add = form.save(commit=False)
            todo_add.todo = todo_note
            todo_add.owner = profile
            todo_add.save()
            return redirect('todos')
        
    context = {'page':page, 'todos':todos}
    return render(request, 'todos/todos.html', context)