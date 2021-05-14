from django.template import Library
from products.models import Product
from ..utils import City

register = Library()


@register.simple_tag
def city_list():
    list = []
    cities = City()
    for c in cities.CITY_LIST:
        list.append(c[1])
    return list


@register.simple_tag
def current_user_products(user):
    object_list = Product.objects.filter(owner=user)
    return [item.name for item in object_list]
