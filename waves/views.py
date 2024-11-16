from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Wave
from .forms import EditWaveForm
# Create your views here.

forbidden_msg = 'No tienes permiso para acceder a esta página.'

@login_required
def wave_detail(request, wave_id):
    wave = Wave.objects.get(id=wave_id)
    return render(request, 'waves/wave_detail.html', dict(wave=wave))

@login_required
def edit_wave(request, wave_id):
    wave = Wave.objects.get(id=wave_id)
    if request.user != wave.user:
        return HttpResponseForbidden(forbidden_msg)

    if request.method == 'POST':
        if (form := EditWaveForm(request.POST, instance=wave)).is_valid():
            wave = form.save(commit=False)
            wave.user = request.user
            wave.save()
            return redirect('waves:wave-detail', wave.pk)
    else:
        form = EditWaveForm(instance=wave)

    return render(request, 'waves/edit_wave.html', dict(wave=wave, form=form))

@login_required
def delete_wave(request, wave_id):
    wave = Wave.objects.get(id=wave_id)
    if request.user != wave.user:
        return HttpResponseForbidden(forbidden_msg)
    wave.delete()
    return render(request, 'waves/delete_wave.html', dict(wave=wave)) 