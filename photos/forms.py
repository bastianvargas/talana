from django import forms
from django.forms import ModelForm

#models
from .models import Photo

class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ['nick_name', 'pet_name', 'photo']
