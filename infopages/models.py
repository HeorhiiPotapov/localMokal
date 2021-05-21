from django.db import models


class InfoBlock(models.Model):
    ABOUT = 0
    RULES = 1
    FORSALLERS = 2
    PAGES = (
        (0, 'About'),
        (1, 'Rules'),
        (2, 'For sallers')
    )
    page = models.CharField(max_length=11, choices=PAGES, default=ABOUT)
    image = models.ImageField(upload_to="infopages_img")
    first_title = models.CharField(max_length=100)
    first_text = models.TextField(max_length=200)
    second_title = models.CharField(max_length=100, null=True, blank=True)
    second_text = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.page.name
