from django.db import models
from django.core.validators import FileExtensionValidator


class SocialLink(models.Model):
    url = models.CharField(max_length=250)
    name = models.CharField(max_length=25)
    image = models.FileField(
        upload_to="social_links",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])

    def __str__(self):
        return self.name
