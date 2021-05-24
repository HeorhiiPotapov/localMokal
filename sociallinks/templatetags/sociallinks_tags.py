from django.template import Library
from sociallinks.models import SocialLink

register = Library()


@register.simple_tag
def social_links():
    return SocialLink.objects.all()
