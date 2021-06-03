from django.views.generic import TemplateView
from products.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class SubscribeView(LoginRequiredMixin, TemplateView):
    template_name = 'subscribe/subscribe.html'

    def post(self, *args, **kwargs):
        cat_id = self.request.POST.get('subscribe')
        print(self.request.POST)
        for i in cat_id:
            cat = Category.objects.get(id=int(i))
            if cat:
                self.request.user.profile.subscribed_to.add(cat)
            else:
                self.request.user.profile.subscribed_to.remove(cat)
        return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent__isnull=True)
        return context
