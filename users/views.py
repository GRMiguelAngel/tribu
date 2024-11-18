from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from echos.models import Echo

from .forms import EditProfileForm
from .models import Profile

# Create your views here.

forbidden_msg = 'No tienes permiso para acceder a esta página.'


@login_required
def profile_list(request):
    users = User.objects.all()
    return render(request, 'users/profile_list.html', dict(users=users))


@login_required
def user_profile(request, username):
    detailed_user = User.objects.get(username=username)
    echos = detailed_user.echos.all().order_by('-created_at')[:5]
    return render(request, 'users/user_profile.html', dict(detailed_user=detailed_user, echos=echos))

@login_required
def my_profile(request):
    return redirect('users:user-profile', request.user)



@login_required
def user_echo_profile(request, username):
    detailed_user = User.objects.get(username=username)
    echos = detailed_user.echos.all().order_by('-created_at')
    return render(request, 'users/user_profile.html', dict(detailed_user=detailed_user, echos=echos))


@login_required
def edit_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    if request.user != profile.user:
        return HttpResponseForbidden(forbidden_msg)

    if request.method == 'POST':
        if (form := EditProfileForm(request.POST, request.FILES, instance=profile)).is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('users:user-profile', user)
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', dict(profile=profile, form=form))
