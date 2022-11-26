from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photo', kwargs={'pk': self.object.pk})


class UpdatePhoto(UserPassesTestMixin, UpdateView):
    template_name = 'update_photo.html'
    model = Photo
    form_class = PhotoForm
    context_object_name = 'photo'

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('webapp.change_photo')

    def get_success_url(self):
        return reverse('photo', kwargs={'pk': self.object.pk})


class DeletePhoto(UserPassesTestMixin, DeleteView):
    template_name = 'delete_photo.html'
    model = Photo
    context_object_name = 'photo'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('webapp.delete_photo')

