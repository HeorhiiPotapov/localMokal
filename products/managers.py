from django.db.models import Q, Manager


class ProductManager(Manager):

    """ Basic Product manager whose impleement some required staff """

    def all(self):
        """ specify all active products  """
        qs = super().get_queryset()
        return qs.filter(is_active=True)

    def with_discount(self):
        qs = self.all().filter(
            discount__isnull=False
        )
        return qs
