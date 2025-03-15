from django.shortcuts import render
from .models import Profile



def profile(request, username):
    profile = Profile.objects.get(username=username)
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)
