from django import forms
from products.utils import City

city = City()


class SubscribeForm(forms.Form):
    name = forms.CharField()
    val = forms.CharField()
    cho = forms.MultipleChoiceField(choices=city.CITY_LIST, widget=forms.CheckboxSelectMultiple())
