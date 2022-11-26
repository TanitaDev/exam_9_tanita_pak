from django.views.generic import ListView

from webapp.models import Photo


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'photos'
    model = Photo
    queryset = Photo.objects.order_by('created_at')
