from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.profile_list, name='user-list'),
    path('@me/', views.my_profile, name='my-profile'),
    path('<str:username>/', views.user_profile, name='user-profile'),
    path('<str:username>/echos/', views.user_echo_profile, name='user-echo-profile'),
    path('<str:username>/edit/', views.edit_profile, name='edit-profile'),
]
