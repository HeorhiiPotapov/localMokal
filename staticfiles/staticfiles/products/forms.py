from django import forms
from .models import Product, Image


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('is_active', 'owner', 'timestamp')


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image',)
