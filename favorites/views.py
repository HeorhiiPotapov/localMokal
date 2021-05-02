from django.shortcuts import render, redirect
from products.models import Product
from django.views import generic


class FavoriteListView(generic.TemplateView):
    template_name = 'favorite.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite_ids = self.request.session.get('favorites')
        if len(favorite_ids) > 0:
            context['products'] = Product.objects.filter(id__in=favorite_ids)
        return context


def add_to_favorite(request, product_id):
    session = request.session
    favorites = session.get('favorites')
    if not favorites:
        favorites = session['favorites'] = list()
    if int(product_id) in favorites:
        del favorites[favorites.index(int(product_id))]
    else:
        favorites.append(int(product_id))
    request.session.modified = True
    return redirect('products:favorite_list')
