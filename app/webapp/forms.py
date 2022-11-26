from django import forms

from webapp.models import Photo


class PhotoForm(forms.ModelForm):
    image = forms.ImageField(label='Фото', required=True)
    signature = forms.CharField(label='Подпись', required=True, widget=forms.Textarea)

    class Meta:
        model = Photo
        exclude = ['author']


class FavouriteForm(forms.Form):
    note = forms.CharField(max_length=50, required=True, label='Избранное')
