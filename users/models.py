from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile'
    ) 
    avatar = models.ImageField(
        upload_to='Avatar', null=True, blank=True, default='avatars/noavatar.png'
    )
    bio = models.TextField(max_length=300, blank=True, null=True)
