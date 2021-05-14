from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Product
from .forms import ProductForm
# from .mixins import IsOwnerMixin
from django.contrib.auth.models import AnonymousUser
# from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import City


class MainPageView(generic.TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent__isnull=True)
        count = [i for i in range(1, 101)]
        """ create model method for discount products """
        context["products"] = Product.objects.filter(discount__in=count)[:8]
        return context


class ProductListView(generic.ListView):
    """
    product list queryset can be a filtered by category
    name, or include all products ordered by creation date
    """
    model = Product
    template_name = 'products/list.html'
    paginate_by = 12

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
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('query')
        region = self.request.GET.get('region')

        print(query, region)
        if query:
            qs = qs.filter(
                Q(name__icontains=query) | Q(city=region)
            )
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
        form = ProductForm(request.POST, request.FILES)

        first_img = [i for i in request.FILES.keys()][0]
        main_img = request.FILES[first_img]

        if form.is_valid():
            new = form.save(commit=False)
            new.main_image = main_img
            new.owner = request.user
            new.save()
            return redirect(reverse('products:detail', kwargs={'pk': new.pk}))
    form = ProductForm()
    categories = Category.objects.all()
    return render(request, 'products/add_page.html', {
        'form': form,
        'categories': categories
    })

# disc_exp = data['discount_expiry']
# disc = data['discount']
# disc_text = data['discount_overview']
# overview = data['overview']
# city = data['city']
# cat = data['category']
# name = data['name']
# price = data['price']
# disc_exp = data['discount_expiry']
# disc = data['discount']
# disc_text = data['discount_overview']
