from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from webapp.views.base import IndexView
from webapp.views.photo import PhotoDetail

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>', PhotoDetail.as_view(), name='photo')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)