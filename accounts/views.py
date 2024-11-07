from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from .forms import SignupForm

# Create your views here.


def user_signup(request):
    if request.method == 'POST':
        if (form := SignupForm(request.POST)).is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', dict(form=form))


def user_logout(request):
    logout(request)

    return redirect('home')
