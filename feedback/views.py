from django.shortcuts import render
from django.views import generic


class NewFeedbackView(generic.TemplateView):
    template_view = 'feedback/new.html'

    def post(self, *args, **kwargs):
        data = self.request.POST

