from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):
    longitude = models.FloatField(verbose_name='Долгота', default=0.0)
    latitude = models.FloatField(verbose_name='Широта', default=0.0)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    sex = models.CharField(max_length=1, choices=[('m', 'Male'), ('f', 'Female')], default='m')
    who_likes = models.ManyToManyField("self", related_name='whom_liked', symmetrical=False, null=True, blank=True)

    class Meta:
        db_table = 'clients'
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.username}'


