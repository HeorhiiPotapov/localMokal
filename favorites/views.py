from products.models import Product
from django.views import generic
from django.http import JsonResponse


class FavoriteListView(generic.TemplateView):
    # template_name = 'favorites/favorite.html'
    template_name = 'products/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite_ids = self.request.session.get('favorites')
        if favorite_ids:
            context['page_obj'] = Product.objects.filter(id__in=favorite_ids)
        return context


def add_to_favorite(request, product_id):
    favorites = request.session.get('favorites')
    if request.is_ajax():
        if not favorites:
            favorites = request.session['favorites'] = list()
        if int(product_id) in favorites:
            del favorites[favorites.index(int(product_id))]
        else:
            favorites.append(int(product_id))
        request.session.modified = True
        return JsonResponse({'is_favorite': int(product_id) in favorites})
    return JsonResponse({'is_favorite': int(product_id) in request.session})
