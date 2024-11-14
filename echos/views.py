from django.shortcuts import redirect, render

from waves.forms import AddWaveForm

from .forms import AddEchoForm
from .models import Echo

# Create your views here.


def echo_list(request):
    echos = Echo.objects.all().order_by('-created_at')
    return render(request, 'echos/echo_list.html', dict(echos=echos))


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


def echo_detail(request, echo_id, all_waves=False):
    echo = Echo.objects.get(id=echo_id)
    waves = echo.waves.all() if all_waves else echo.waves.all()[:5]
    return render(request, 'echos/echo_detail.html', dict(echo=echo, waves=waves))


def add_wave(request, echo_id):
    if request.method == 'POST':
        if (form := AddWaveForm(request.POST)).is_valid():
            wave = form.save(commit=False)
            wave.user = request.user
            wave.echo = Echo.objects.get(id=echo_id)
            form.save()
            return redirect('echos:echo-detail', echo_id)
    else:
        form = AddEchoForm()
    return render(request, 'waves/add_wave.html', dict(form=form))
