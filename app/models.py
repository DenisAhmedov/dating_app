from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    sex = models.CharField(max_length=1,
                           choices=[('m', 'Male'), ('f', 'Female')],
                           default='m')

    class Meta:
        db_table = 'clients'
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return f'{self.username}'


