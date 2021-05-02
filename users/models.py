from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.utils import City
from products.models import Product


city = City()


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('Почта', unique=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(CustomUser,
                                primary_key=True,
                                related_name='profile',
                                on_delete=models.CASCADE)
    image = models.ImageField("Фото профиля",
                              upload_to="profile_img",
                              default="profile_img/default_profile_img.jpg")
    logo = models.ImageField("Лого",
                             upload_to="profile_logo",
                             null=True,
                             blank=True)
    brand = models.CharField("Бренд",
                             max_length=100,
                             null=True,
                             blank=True)
    city = models.CharField("Город",
                            choices=City.CITY_LIST,
                            max_length=50,
                            null=True,
                            blank=True)
    address = models.CharField("Адресс",
                               max_length=300,
                               null=True,
                               blank=True)
    phone = models.CharField("Телефон",
                             max_length=100,
                             null=True,
                             blank=True)
    country = models.CharField("Страна",
                               max_length=100,
                               null=True,
                               blank=True)
    favorites = models.ManyToManyField(Product,
                                       verbose_name="Избранное")

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
