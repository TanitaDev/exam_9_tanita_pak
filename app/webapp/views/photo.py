from django.views.generic import DetailView

from webapp.models import Photo


class PhotoDetail(DetailView):
    template_name = 'phtoto_detail.html'
    model = Photo
    context_object_name = 'photo'
