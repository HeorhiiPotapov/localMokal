from django.shortcuts import redirect
from .models import SocialLink
from django.views.generic import TemplateView
from .forms import SocialLinkForm


class LinksListView(TemplateView):
    template_name = 'sociallinks/list.html'

    def post(self, *args, **kwargs):
        form = SocialLinkForm(self.request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["links"] = SocialLink.objects.all()
        context["form"] = SocialLinkForm()
        return context
