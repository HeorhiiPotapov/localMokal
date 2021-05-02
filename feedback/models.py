from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Feedback(models.Model):
    username = models.CharField("Имя", max_length=30)
    email = models.EmailField()
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.username
