import json
import random
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView, DetailView, DeleteView
from django.urls import reverse
from .models import Category, Product, Banner
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class MainPageView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent__isnull=True)
        context["products"] = Product.objects.with_discount()[:8]
        return context


class ProductListView(ListView):
    """
    product list queryset can be a filtered by category
    name, or include all products ordered by creation date
    """
    model = Product
    template_name = 'products/list.html'
    paginate_by = 24

    def get_queryset(self, **kwargs):
        category = None
        qs = super().get_queryset(**kwargs)
        cat_slug = self.kwargs.get('cat_slug')
        if cat_slug:
            """
            use get_descendants() to include all children's
            category products in queryset
            """
            category = get_object_or_404(
                Category,
                slug=cat_slug).get_descendants(include_self=True)
            qs = qs.filter(category__in=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_slug = self.kwargs.get('cat_slug')
        if cat_slug:
            context['cat_obj'] = get_object_or_404(
                Category, slug=cat_slug)
        return context


class ProductSearchResult(ListView):
    model = Product
    template_name = 'products/list.html'
    paginate_by = 24

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('query')
        qs = qs.filter(name__icontains=query)
        return qs


def get_products_qs(request):
    if request.is_ajax():
        query = request.GET.get('query')
        products = Product.objects.filter(name__icontains=query)
        counter = 0
        response = dict()
        for item in products:
            context = {
                "name": item.name,
                "link": f"/products/detail/{item.id}/{item.slug}/"
            }
            response[str(counter)] = context
            counter += 1
            return JsonResponse(json.dumps(response), safe=False)
    return JsonResponse({'error': 'all bad'}, status=404)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.get_object().images.all()
        cat = self.get_object().category
        context['sugested'] = Product.objects.filter(
            category=cat).order_by('-timestamp')[:2]
        return context


@login_required
def add_product(request, **kwargs):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        print(product_form.errors)
        if product_form.is_valid():
            new = product_form.save(commit=False)
            new.owner = request.user
            new.save()
            product_form.save_m2m()
            for f in request.FILES.keys():
                new.images.create(image=request.FILES[f])
            """
            discount = (
                request.POST.get('discount')
                or request.POST.get('discount')
                and request.POST.get('expiry')
            ) """
            return redirect(reverse('products:detail',
                                    kwargs={'pk': new.pk,
                                            'slug': new.slug}))
    product_form = ProductForm()
    categories = Category.objects.all()
    return render(request, 'products/create.html', {
        'product_form': product_form,
        'categories': categories})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('adminpanel:main')


class CategoryListView(TemplateView):
    template_name = 'products/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(parent__isnull=True)
        try:
            context["banner"] = random.choice(Banner.objects.all())
        except IndexError:
            pass
        return context
