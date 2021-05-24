from django.db import models


class Page(models.Model):
    ABOUT = 0
    RULES = 1
    FORSALLERS = 2
    PAGE_TYPE_CHOICES = (
        (0, 'About'),
        (1, 'Rules'),
        (2, 'For sallers')
    )
    pagetype = models.CharField(max_length=20, choices=PAGE_TYPE_CHOICES)

    def __str__(self):
        return self.pagetype


class InfoBlock(models.Model):

    page = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name="blocks")
    image = models.ImageField(upload_to="infopages_img", null=True, blank=True)
    video = models.URLField(blank=True, null=True)
    first_title = models.CharField(max_length=100)
    first_text = models.TextField(max_length=200)
    second_title = models.CharField(max_length=100, null=True, blank=True)
    second_text = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.page.name
