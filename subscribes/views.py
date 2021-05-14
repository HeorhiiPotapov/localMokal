from django.views import generic
from .models import Subscribtion
from products.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class SubscribeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'subscribe/subscribe.html'

    def post(self, *args, **kwargs):
        data = self.request.POST
        data_cat = data.getlist('subscriptions_cat')
        cat_ids = [int(i) for i in data_cat]
        cat_qs = Category.objects.filter(id__in=cat_ids)
        new_subscribe = Subscribtion.objects.create(
            user=self.request.user,
            region=data.get('subscription-to-shares__region'),
            social=data.get('socials_subscriptions')
        )
        new_subscribe.save()
        new_subscribe.categories.add(*cat_qs)
        print(data)
        return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent__isnull=True)
        return context
