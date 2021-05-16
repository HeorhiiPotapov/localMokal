from django.views.generic import TemplateView
from .forms import SubscribtionAddForm
from products.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class SubscribeView(LoginRequiredMixin, TemplateView):
    template_name = 'subscribe/subscribe.html'

    def post(self, *args, **kwargs):
        form = SubscribtionAddForm(self.request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            cat_ids = [int(i) for i in self.request.POST.getlist('category')]
            cat_qs = Category.objects.filter(id__in=cat_ids)
            new.categories.add(*cat_qs)
            new.save()
        else:
            print(form.errors)
        return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent__isnull=True)
        return context
