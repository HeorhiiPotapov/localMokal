rom django.db import models

# Create your models here.


class SocialLink(models.Model):
    url = models.CharFiel(max_length=250)
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="social_links")

    def __str__(self):
        return self.name
