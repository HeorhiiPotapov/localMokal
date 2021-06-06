from django.template import Library
from products.models import Category, Product
from ..utils import City

register = Library()


@register.simple_tag
def city_list():
    city_list = [c for c in City.CITY_LIST]
    return city_list


@register.inclusion_tag('products/categories.html')
def get_categories_list(node):
    cat_list = Category.objects.filter(parent__isnull=True)
    return {'cat_list': cat_list}


@register.inclusion_tag('products/parent_cat.html')
def get_childrens(node):
    childrens = Category.objects.filter(parent=node)
    return {'childrens': childrens}


@register.simple_tag(takes_context=True)
def user_products(context):
    request = context['request']
    if request.user.is_authenticated:
        return Product.objects.filter(owner=request.user)
