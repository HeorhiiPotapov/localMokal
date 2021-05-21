from django.template import Library
from products.models import Product
from ..utils import City

register = Library()


@register.simple_tag
def city_list():
    city_list = [c for c in City.CITY_LIST]
    return city_list


@register.simple_tag(takes_context=True)
def favorite_items(context):
    request = context['request']
    favorites = request.session.get('favorites')
    product_ids = []
    if favorites:
        product_ids = Product.objects.filter(
            id__in=[item_id for item_id in favorites])
    return product_ids


@register.simple_tag(takes_context=True)
def user_products(context):
    request = context['request']
    if request.user.is_authenticated:
        return Product.objects.filter(owner=request.user)
