from django.db import models

from django.urls import reverse
from django.core.validators import MinValueValidator, \
    MaxValueValidator
from django.utils import timezone
from decimal import Decimal
from mptt.models import MPTTModel, TreeForeignKey
from .utils import City
from django.conf import settings
from .managers import ProductManager
from datetime import timedelta
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator


class Category(MPTTModel):
    image = models.FileField(
        upload_to="category_img",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])]
    )
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children')
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class MPTTMeta:
        order_insertion_by = ['-timestamp']

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:by_category",
                       kwargs={'pk': self.pk,
                               "cat_slug": self.slug})


def default_discount_expiry():
    return timezone.now() + timedelta(days=30)


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=0)
    slug = models.SlugField(unique=True,
                            editable=False)
    video = models.URLField(null=True,
                            blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="products")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='products')
    overview = models.TextField(max_length=2000)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=20,
                            default=City.ANY,
                            choices=City.CITY_LIST)
    keywords = models.CharField(max_length=100,
                                null=True,
                                blank=True)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
    discount_overview = models.TextField(max_length=200,
                                         null=True,
                                         blank=True)
    expiry_date = models.DateTimeField(default=default_discount_expiry)

    objects = ProductManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(
            self.name + '-' + str(self.id))
        return super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ('-timestamp',)

    def get_absolute_url(self):
        return reverse("products:detail",
                       kwargs={"pk": self.pk,
                               'slug': self.slug})

    def price_after_discount(self):
        new_price = self.price
        if self.discount is not None:
            new_price = self.price - self.price * \
                (self.discount / Decimal('100'))
        return new_price


class Image(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="images")
    image = models.ImageField(upload_to="product_img")
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ('timestamp',)

    def __str__(self):
        return f"{self.product.name}"
