from django.forms import ModelForm
from .models import Subscribtion


class SubscribtionAddForm(ModelForm):
    class Meta:
        model = Subscribtion
        exclude = ['user', 'timestamp']
