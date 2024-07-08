from django.shortcuts import render
from .models import Thought

def thoughts(request):
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = None
    thoughts = Thought.objects.all()
    context = {'profile':profile, 'thoughts':thoughts}
    return render(request, 'thoughts/thoughts.html', context)
