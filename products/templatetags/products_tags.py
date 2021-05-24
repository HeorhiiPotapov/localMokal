from django.template import Library
from products.models import Product
from ..utils import City

register = Library()


@register.simple_tag
def city_list():
    city_list = [c for c in City.CITY_LIST]
    return city_list


@register.simple_tag(takes_context=True)
def user_products(context):
    request = context['request']
    if request.user.is_authenticated:
        return Product.objects.filter(owner=request.user)
