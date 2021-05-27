from django.forms import ModelForm
from .models import Feedback, ProductFeedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ('timestamp',)


class ProductFeedbackForm(ModelForm):
    class Meta:
        model = ProductFeedback
        fields = ('text',)
