from django import forms

from webapp.models import Photo


class PhotoForm(forms.ModelForm):
    image = forms.ImageField(label='Фото', required=True)
    signature = forms.CharField(label='Подпись', required=True, widget=forms.Textarea)

    class Meta:
        model = Photo
        fields = ['image', 'signature', 'author']
