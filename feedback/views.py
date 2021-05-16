from django.views.generic import TemplateView
from .forms import FeedbackForm
from django.http import HttpResponseRedirect


class NewFeedbackView(TemplateView):
    template_name = 'feedback/create.html'

    def post(self, *args, **kwargs):
        form = FeedbackForm(self.request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(self.request.path_info)
