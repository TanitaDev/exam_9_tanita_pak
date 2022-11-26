from django.views.generic import ListView

from webapp.forms import FavouriteForm
from webapp.models import Photo


class IndexView(ListView):
    template_name = 'index.html'
    model = Photo

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['favourite_form'] = FavouriteForm()
        context['photos'] = Photo.objects.order_by('created_at')
        return context
