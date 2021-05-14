from django.db import models
from products.models import Category
from django.contrib.auth import get_user_model
from django.utils import timezone

# need to relocate utils to the app with default values
from products.utils import City

User = get_user_model()


class Subscribtion(models.Model):
    EMAIL = 'email'
    TG = 'telegram'
    VIBER = 'viber'
    SOCIAL_CHOICES = (
        ('email', 'Email'),
        ('telegram', 'Telegram'),
        ('viber', 'Viber')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscribtions")
    region = models.CharField(
        max_length=50, choices=City.CITY_LIST, default=City.ANY)
    social = models.CharField(
        max_length=10, choices=SOCIAL_CHOICES, default=EMAIL)
    categories = models.ManyToManyField(Category, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user.email)

    class Meta:
        ordering = ('-timestamp',)
