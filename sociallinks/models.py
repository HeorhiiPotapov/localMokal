from django.db import models


class SocialLink(models.Model):
    url = models.CharField(max_length=250)
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="social_links")

    def __str__(self):
        return self.name
