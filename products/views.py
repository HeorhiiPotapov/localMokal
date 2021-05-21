from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Product, Image, Discount
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
            qs = qs.filter(Q(name__icontains=query, city=region))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['query'] = self.request.GET.get('query')
        context['region'] = self.request.GET.get('region')
        return context


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
        # start creating product
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid() and len(request.FILES) > 0:
            new = form.save(commit=False)
            new.owner = request.user
            new.save()

        # start saving image/images
            files = request.FILES
            file_list = list(request.FILES.keys())
            for f in file_list:
                Image.objects.create(product=new, image=files[f]).save()

        # start creating discount for product
            discount = request.POST.get('discount')
            discount_expiry = request.POST.get('discount_expiry')
            discount_overview = request.POST.get('discount_overview')
            if discount:
                new_discount = Discount.objects.create(
                    product=new,
                    expiry_date=discount_expiry,
                    overview=discount_overview
                )
                new_discount.save()

            return redirect(reverse('products:detail',
                                    kwargs={'pk': new.pk, 'slug': new.slug}))
    form = ProductForm()
    categories = Category.objects.all()
    return render(request, 'products/add_page.html', {'form': form,
                                                      'categories': categories})
