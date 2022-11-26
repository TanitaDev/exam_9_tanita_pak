from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoDetail(DetailView):
    template_name = 'detail_photo.html'
    model = Photo
    context_object_name = 'photo'


class CreatePhoto(LoginRequiredMixin, CreateView):
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


class DeletePhoto(DeleteView):
    template_name = 'delete_photo.html'
    model = Photo
    context_object_name = 'photo'
    success_url = reverse_lazy('index')
