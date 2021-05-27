from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from products.models import Product

User = get_user_model()


class Feedback(models.Model):
    """ Feedback class Docstrings """
    name = models.CharField("Имя", max_length=30)
    email = models.EmailField()
    text = models.TextField(max_length=600)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.name


class ProductFeedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receiver')
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    text = models.TextField(max_length=600)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"dialog: {self.sender.email} => {self.receiver.email}"
