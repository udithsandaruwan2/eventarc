from django.shortcuts import render

def thoughts(request):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request, 'thoughts/thoughts.html', context)
