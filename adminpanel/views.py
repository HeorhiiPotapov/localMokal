from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView
from products.models import Category, Product
from products.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()


class MainPage(LoginRequiredMixin, ListView):
    template_name = 'adminpanel/main.html'
    paginate_by = 10
    context_object_name = 'products'

    def get_queryset(self):
        products = Product.objects.filter(owner=self.request.user)
        return products


class ProductUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'adminpanel/product_edit.html'
    model = Product
    # fields = ('name', 'price')
    form_class = ProductForm
    success_url = reverse_lazy('adminpanel:main')

    def form_valid(self, form):
        updated = form.save(commit=False)
        updated.owner = User.objects.get(id=self.request.user.id)
        updated.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
