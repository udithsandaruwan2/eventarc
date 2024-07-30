from django.shortcuts import render

def todoList(request):
    page = 'todos'
    
    if request.method == 'POST':
        return redir
    context = {'page':page}
    return render(request, 'todos/todos.html', context)