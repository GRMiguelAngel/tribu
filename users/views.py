from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Profile

# Create your views here.


@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profile_list.html', dict(profiles=profiles))


@login_required
def user_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return render(request, 'users/user_profile.html', dict(profile=profile, user=user))
