from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.urls import reverse
from .models import Category, Product, Image
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


class MainPageView(generic.TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent__isnull=True)
        context["products"] = Product.objects.with_discount()[:8]
        return context


class ProductListView(generic.ListView):
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


class ProductSearchResult(generic.ListView):
    model = Product
    template_name = 'products/list.html'
    paginate_by = 24

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('query')
        region = self.request.GET.get('region-inp')
        if region or query:
            qs = qs.filter(Q(name__icontains=query) | Q(city=query))
        elif region and query:
            qs = qs.filter(Q(name__icontains=query) & Q(city=query))
        return qs


class ProductDetailView(generic.DetailView):
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
