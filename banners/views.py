from django.shortcuts import render
from .models import UserBanner
from django.views.generic import TemplateView


class BannerListView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banners"] = UserBanner.objects.filter(
            user=self.request.user
        )
        return context
