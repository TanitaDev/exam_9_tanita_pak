from django.db import models
from django.contrib.auth import get_user_model

from webapp.models import Favourite


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    favourite = models.ManyToManyField(to='webapp.Photo', verbose_name='Избранные', related_name='favs')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
