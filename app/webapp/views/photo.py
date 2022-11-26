from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoDetail(DetailView):
    template_name = 'detail_photo.html'
    model = Photo
    context_object_name = 'photo'


class CreatePhoto(CreateView):
    template_name = 'create_photo.html'
    model = Photo
    form_class = PhotoForm

    def get_success_url(self):
        return reverse('index')


class UpdatePhoto(UpdateView):
    template_name = 'update_photo.html'
    model = Photo
    form_class = PhotoForm
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('photo', kwargs={'pk': self.object.pk})
