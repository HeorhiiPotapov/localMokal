from django.db.models import Q, Manager


class ProductManager(Manager):
    def all(self):
        """ specify all active products  """
        qs = super().get_queryset()
        return qs.filter(is_active=True)

    def with_discount(self):
        qs = self.all().filter(
            Q(discount__gt=0) | Q(lte__=100)
        )
        return qs
