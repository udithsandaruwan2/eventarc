from .models import Note
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchNotes(request):
    search_query = '' 
    if request.GET.get('search'):
        search_query = request.GET.get('search', '')
        
    # notes = Note.objects.filter(name__icontains=search_query)
    
    notes = Note.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) 
    )
    
    return notes, search_query