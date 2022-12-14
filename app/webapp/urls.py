from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from webapp.views.base import IndexView
from webapp.views.favourite import FavouriteView
from webapp.views.photo import PhotoDetail, CreatePhoto, UpdatePhoto, DeletePhoto

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>', PhotoDetail.as_view(), name='photo'),
    path('create/', CreatePhoto.as_view(), name='create'),
    path('update/<int:pk>', UpdatePhoto.as_view(), name='update'),
    path('delete/<int:pk>', DeletePhoto.as_view(), name='delete'),
    path('favourite/<int:pk>/', FavouriteView.as_view(), name='favourite')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
