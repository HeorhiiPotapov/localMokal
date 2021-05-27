from django.db import models
from products.models import default_discount_expiry
from django.contrib.auth import get_user_model

User = get_user_model()


class UserBanner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='banners')
    is_active = models.BooleanField(default=True)
    expiry = models.DateTimeField(default=default_discount_expiry)

    def __str__(self):
        return self.user.email
