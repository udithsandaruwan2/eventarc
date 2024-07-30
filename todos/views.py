from django.shortcuts import render

def todoList(request):
    page = 'todos'
    context = {'page':page}
    return render(request, 'todos/todos.html', context)