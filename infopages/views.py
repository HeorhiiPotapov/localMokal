from .models import InfoBlock
from django.views.generic import TemplateView


class AboutUsPage(TemplateView):
    template_name = 'infopages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutUsPageCreate(TemplateView):
    template_name = 'infopages/about_add.html'

    def post(self):
        pass
