from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.safestring import mark_safe
from django.utils.html import format_html


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

    def image_content(self):
        file = open(self.image.path)
        data = format_html(file.read())
        file.close()
        return mark_safe(data)
