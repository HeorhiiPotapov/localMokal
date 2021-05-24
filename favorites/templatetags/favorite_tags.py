from django.template import Library
from products.models import Product

register = Library()


@register.simple_tag(takes_context=True)
def favorite_items(context):
    request = context['request']
    favorites = request.session.get('favorites')
    product_ids = []
    if favorites:
        product_ids = Product.objects.filter(
            id__in=[item_id for item_id in favorites])
    return product_ids
