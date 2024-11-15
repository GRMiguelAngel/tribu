from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from waves.forms import AddWaveForm

from .forms import AddEchoForm, EditEchoForm
from .models import Echo

# Create your views here.


@login_required
def echo_list(request):
    echos = Echo.objects.all().order_by('-created_at')
    return render(request, 'echos/echo_list.html', dict(echos=echos))


@login_required
def add_echo(request):
    if request.method == 'POST':
        if (form := AddEchoForm(request.POST)).is_valid():
            echo = form.save(commit=False)
            echo.user = request.user
            form.save()
            return redirect('echos:echo-list')
    else:
        form = AddEchoForm()
    return render(request, 'echos/add_echo.html', dict(form=form))


@login_required
def edit_echo(request, echo_id: str):
    echo = Echo.objects.get(id=echo_id)
    print(request.user, echo.user)
    if request.user != echo.user:
        return HttpResponseForbidden('nono no puedes')

    if request.method == 'POST':
        if (form := EditEchoForm(request.POST, instance=echo)).is_valid():
            echo = form.save(commit=False)
            echo.user = request.user
            echo.save()
            return redirect('echos:echo-detail', echo.pk)
    else:
        form = EditEchoForm(instance=echo)

    return render(request, 'echos/edit_echo.html', dict(echo=echo, form=form))



@login_required
def delete_echo(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    echo.delete()
    return render(request, 'echos/delete_echo.html', dict(echo=echo))


@login_required
def echo_detail(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    waves = echo.waves.all()[:5]
    return render(request, 'echos/echo_detail.html', dict(echo=echo, waves=waves))


@login_required
def add_wave(request, echo_id):
    if request.method == 'POST':
        if (form := AddWaveForm(request.POST)).is_valid():
            wave = form.save(commit=False)
            wave.user = request.user
            wave.echo = Echo.objects.get(id=echo_id)
            form.save()
            return redirect('echos:echo-detail', echo_id)
    else:
        form = AddWaveForm()
    return render(request, 'waves/add_wave.html', dict(form=form))


@login_required
def echo_wave_list(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    waves = echo.waves.all()
    return render(request, 'echos/echo_detail.html', dict(echo=echo, waves=waves))
