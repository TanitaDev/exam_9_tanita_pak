from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import FormView

from webapp.forms import FavouriteForm
from webapp.models import Photo, Favourite


class FavouriteView(FormView):
    form_class = FavouriteForm

    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            note = form.cleaned_data.get('note')
            user = request.user
            Favourite.objects.create(user=user, photo=photo, note=note)
        return redirect('index')

