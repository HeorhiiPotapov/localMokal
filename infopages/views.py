from django.shortcuts import render
from django.views import generic


InfoPages = generic.TemplateView.as_view(template_name="some.html")
