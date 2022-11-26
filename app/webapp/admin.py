from django.contrib import admin

from webapp.models import Photo, Favorite


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'signature', 'author', 'created_at']


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Favorite, FavoriteAdmin)
