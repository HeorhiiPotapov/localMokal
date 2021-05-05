from django.views import generic
from .models import Subscribtion
from products.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import SubscribeForm


class SubscribeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'subscribe/subscribe.html'

    def post(self, *args, **kwargs):
        data = self.request.POST
        print(data)
        data_cat = data.getlist('subscriptions_cat')
        cat_ids = [int(i) for i in data_cat]
        cat_qs = Category.objects.filter(id__in=cat_ids)
        print(data_cat)
        print(**kwargs)
        new_subscribe = Subscribtion.objects.create(
            user=self.request.user,
            # region=data.get('region'),
            # use_email=data.get('use_email'),
            # use_telegram=data.get('use_telegram'),
            # use_viber=data.get('use_viber')
        )
        new_subscribe.save()
        new_subscribe.categories.add(*cat_qs)
        return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(level=0)
        context['form'] = SubscribeForm()
        return context
