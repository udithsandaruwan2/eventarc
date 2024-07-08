from django.shortcuts import render
from .models import Note

def notes(request):
    page = "notes"
    profile = request.user.profile
    notes = Note.objects.filter(owner=profile)
    context = {'page':page, 'notes':notes}
    return render(request, 'notes/notes.html', context)
