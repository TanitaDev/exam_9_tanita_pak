from django.contrib import admin

from webapp.models import Photo, Favourite


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'signature', 'author', 'created_at']


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'photo']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Favourite, FavouriteAdmin)
