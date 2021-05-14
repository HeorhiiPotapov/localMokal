from django.shortcuts import render
from django.views import generic
from .models import Feedback
from django.http import HttpResponseRedirect


class NewFeedbackView(generic.TemplateView):
    template_name = 'feedback/create.html'

    def post(self, *args, **kwargs):
        Feedback.objects.create(name=self.request.POST['name'],
                                email=self.request.POST['email'],
                                text=self.request.POST['text']).save()
        return HttpResponseRedirect(self.request.path_info)
