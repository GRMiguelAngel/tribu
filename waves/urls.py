from django.urls import path
from . import views

app_name = 'waves'

urlpatterns = [
    path('<wave_id>/', views.wave_detail, name='wave-detail'),
    path('<wave_id>/edit/', views.edit_wave, name='edit-wave'),
    path('<wave_id>/delete/', views.delete_wave, name='delete-wave'),
]
