from django.contrib import admin
from .models import Echo
from waves.models import Wave

# Register your models here.

@admin.register(Echo)
class EchoAdmin(admin.ModelAdmin):
    list_display = ['content', 'user']

@admin.register(Wave)
class WaveAdmin(admin.ModelAdmin):
    list_display = ['content', 'user']