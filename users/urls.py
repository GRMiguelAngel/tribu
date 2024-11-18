from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('', views.profile_list, name='profile-list'),
    path('<str:username>/', views.user_profile, name='user-profile'),
]
