from django.db import models
from products.models import Category
from django.contrib.auth import get_user_model
from django.utils import timezone
from products.utils import City

User = get_user_model()


class Subscribtion(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscribtions")
    region = models.CharField(
        max_length=50, choices=City.CITY_LIST, default=City.ANY)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    viber = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user.email)

    class Meta:
        ordering = ('-timestamp',)
