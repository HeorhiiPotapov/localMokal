from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('is_active', 'owner', 'timestamp',
                   'slug', 'expiry_date', 'discount')
