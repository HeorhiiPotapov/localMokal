from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, \
    MaxValueValidator
from django.utils import timezone
from decimal import Decimal
from mptt.models import MPTTModel, TreeForeignKey
from .utils import City
from django.conf import settings
from datetime import datetime, timedelta
from .managers import ProductManager

city = City()


def set_discount_expiry():
    result = str(datetime.now) + str(timedelta(days=30))
    return result


class Category(MPTTModel):
    """
    Product category class
    """
    image = models.FileField("Лого категории",
                             upload_to="category_img",
                             null=True,
                             blank=True)
    name = models.CharField("Название",
                            max_length=300)
    slug = models.SlugField("Url",
                            max_length=300,
                            unique=True)
    parent = TreeForeignKey("self",
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children',
                            verbose_name="Категория верхнего уровня")
    is_active = models.BooleanField("Статус",
                                    default=True)

    class MPTTMeta:
        order_insertion_by = ['slug']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:by_category",
                       kwargs={"slug": self.slug})


class Product(models.Model):
    """
    Product class
    """
    name = models.CharField("Название", max_length=300)
    price = models.DecimalField("Цена",
                                max_digits=10,
                                decimal_places=2,
                                default=0)
    discount = models.IntegerField("Дисконт",
                                   null=True,
                                   blank=True,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
    discount_expiry = models.DateTimeField("Дата окончания акции",
                                           default=set_discount_expiry)
    main_image = models.ImageField("Изображение",
                                   upload_to="product_img")
    video = models.URLField("Ссылка на видео",
                            null=True,
                            blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="products",
                              verbose_name="Владелец")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='products',
                                 verbose_name="Категория")
    overview = models.TextField("Описание",
                                max_length=2000)
    is_active = models.BooleanField("Статус",
                                    default=False)
    timestamp = models.DateTimeField("Дата добавления",
                                     default=timezone.now)
    city = models.CharField("Город",
                            max_length=20,
                            choices=city.CITY_LIST,
                            default=city.ANY)

    objects = ProductManager()

    class Meta:
        verbose_name = "Товар/Акция"
        verbose_name_plural = "Товары/Акции"
        # ordering = ('-timestamp',)

    def price_after_discount(self):
        new_price = self.price
        if self.discount is not None:
            new_price = self.price - self.price * \
                (self.discount / Decimal('100'))
        return new_price

    def get_absolute_url(self):
        return reverse("products:detail",
                       kwargs={"pk": self.pk})


class Image(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="images")
    image = models.ImageField("Изображение",
                              upload_to="product_img")
    is_active = models.BooleanField("Статус",
                                    default=True)
    timestamp = models.DateTimeField("Дата добавления",
                                     default=timezone.now)

    class Meta:
        verbose_name = "Дополнительное фото"
        verbose_name_plural = "Дополнительные фото"

    def __str__(self):
        return f"{self.product.id}"
