from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='img', blank=False, null=False)
    signature = models.CharField(verbose_name='Подпись', max_length=1000, blank=False, null=False)
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    author = models.ForeignKey(
        verbose_name='Автор', to=get_user_model(), related_name='photos', on_delete=models.CASCADE, blank=False,
        null=False
    )


class Favorite(models.Model):
    user = models.ForeignKey(to=User, related_name='favorite', verbose_name='Пользователь', null=False,
                             on_delete=models.CASCADE)
    image = models.ForeignKey(to=Photo, related_name='favourite_users', verbose_name='Избранное', null=False,
                              on_delete=models.CASCADE)
