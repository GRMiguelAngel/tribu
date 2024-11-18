from django.contrib import admin

from waves.models import Wave

from .models import Echo

from users.models import Profile
# Register your models here.


@admin.register(Echo)
class EchoAdmin(admin.ModelAdmin):
    list_display = ['content', 'user']


@admin.register(Wave)
class WaveAdmin(admin.ModelAdmin):
    list_display = ['content', 'user']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['bio']