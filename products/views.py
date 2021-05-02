from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Product
from .forms import ProductForm
from .mixins import IsOwnerMixin
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


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
    paginate_by = 2

    def get_queryset(self, **kwargs):
        category = None
        qs = super().get_queryset()
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


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = self.get_object().category
        context['user'] = self.request.user.is_authenticated or AnonymousUser()

        context['sugested'] = Product.objects.filter(
            category=cat).order_by('-timestamp')[:2]
        return context


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:all')

    def form_valid(self, form):
        if form.is_valid():
            p_form = form.save(commit=False)
            p_form.owner = self.request.user
            p_form.save()
            return super().form_valid(form)


@login_required
def add_product(request):
    if request.method == 'POST':
        request_obj = request.POST
        for key in request_obj:
            print(key + '==>>' + request_obj.get(key))
        pass
    return render(request, 'products/create.html')
