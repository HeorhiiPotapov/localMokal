from django.shortcuts import render
from django.views import generic
from products.models import Category


class SubscribeView(generic.TemplateView):
    template_name = 'subscribe/subscribe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(level=0)
        return context
