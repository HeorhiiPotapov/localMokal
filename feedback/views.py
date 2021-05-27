from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .forms import FeedbackForm, ProductFeedbackForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from .models import ProductFeedback
from django.db.models import Q


class NewFeedbackView(TemplateView):
    template_name = 'feedback/create.html'

    def post(self, *args, **kwargs):
        form = FeedbackForm(self.request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(self.request.path_info)


class ProductFeedbackView(LoginRequiredMixin, TemplateView):
    template_name = 'feedback/product_feedback.html'

    def post(self, *args, **kwargs):
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        feed_form = ProductFeedbackForm(self.request.POST)
        if feed_form.is_valid():
            new_feed = feed_form.save(commit=False)
            new_feed.sender = self.request.user
            new_feed.receiver = product.owner
            new_feed.save()
            return HttpResponseRedirect('feedback:dialog')
        else:
            return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(id=self.kwargs['product_id'])
        context["product_id"] = product.id
        context["feed_form"] = ProductFeedbackForm()
        return context


class Dialog(LoginRequiredMixin, TemplateView):
    template_name = 'feedback/dialog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        product = Product.objects.filter(id=self.kwargs['product_id'])
        context['product'] = product
        context["messages"] = ProductFeedback.objects.filter(
            Q(product=product, sender=user) | Q(product=product, receiver=user)
        )
        return context
