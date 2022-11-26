from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='img', blank=False, null=False)
    signature = models.CharField(verbose_name='Подпись', max_length=1000, blank=False, null=False)
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), verbose_name='Автор', related_name='photos', on_delete=models.CASCADE, blank=False, null=False
    )
    users = models.ManyToManyField(through='webapp.Favourite', to=User, related_name='us_photos')

    def __str__(self):
        return f'{self.image} {self.author}'


class Favourite(models.Model):
    user = models.ForeignKey(to=User, related_name='favorite', verbose_name='Пользователь', null=False,
                             on_delete=models.CASCADE)
    photo = models.ForeignKey(to=Photo, related_name='favourite_users', verbose_name='Избранное', null=False,
                              on_delete=models.CASCADE)
    note = models.CharField(max_length=50, verbose_name='Текстовая заметка', null=False, blank=True)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return f'{self.user} {self.photo}'

