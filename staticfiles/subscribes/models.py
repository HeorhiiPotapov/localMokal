from django.db import models
from products.models import Category
from django.contrib.auth import get_user_model
from django.utils import timezone

# need to relocate utils to the app with default values
from products.utils import City

User = get_user_model()
# cities = City()


class Subscribtion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscribtions")
    region = models.CharField(max_length=50, choices=City.CITY_LIST, default=City.ANY)
    use_email = models.BooleanField(default=False)
    use_viber = models.BooleanField(default=False)
    use_telegram = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.use_viber is False and self.use_telegram is False:
            self.use_email = True
        super(Subscribtion, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-timestamp',)
