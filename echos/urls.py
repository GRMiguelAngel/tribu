from django.urls import path

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_echo, name='add-echo')
]
