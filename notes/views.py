from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.contrib import messages
from .utils import searchNotes
from .models import Todo

def notes(request):
    page = "notes"
    profile = request.user.profile
    form = NoteForm()
    notes, search_query = searchNotes(request)
    
    # Retrieve all todos for the current profile
    all_todos = Todo.objects.filter(owner=profile)
    
    if request.method == 'POST':
        form = NoteForm(request.POST)
        selected_todo_ids = request.POST.getlist('todo_ids')
        
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = profile
            note.save()  # Save the note instance first to get the ID
            
            # Now add the selected todos to the note
            todos = Todo.objects.filter(id__in=selected_todo_ids)
            note.todo_field.set(todos)  # Use set() to assign the ManyToMany field
            note.save()
            
            messages.success(request, 'Note added successfully!')
            return redirect('notes')
        
    context = {
        'page': page,
        'notes': notes,
        'form': form,
        'search_query': search_query,
        'todos': all_todos  # Pass all todos for rendering
    }
    return render(request, 'notes/notes.html', context)
