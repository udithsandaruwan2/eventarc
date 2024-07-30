from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.contrib import messages
from .utils import searchNotes

def notes(request):
    page = "notes"
    form = NoteForm()
    
    profile = request.user.profile
    
    notes, search_query = searchNotes(request)
    
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = profile
            note.save()
            messages.success(request, 'Note added successfully!')
            return redirect('notes')
        
    profile = request.user.profile
    # notes = Note.objects.filter(owner=profile)
    context = {'page':page, 'notes':notes, 'form':form, 'search_query':search_query}
    return render(request, 'notes/notes.html', context)
