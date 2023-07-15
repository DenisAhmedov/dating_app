from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    sex = models.CharField(max_length=1,
                           choices=[('m', 'Male'), ('f', 'Female')],
                           default='m')

    def __str__(self):
        return f'{self.username}'


