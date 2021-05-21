from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.utils import City
from products.models import Category


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
    user = models.OneToOneField(CustomUser, primary_key=True,
                                related_name='profile',
                                on_delete=models.CASCADE)
    image = models.ImageField(default="profile_img/default_profile_img.jpg",
                              upload_to="profile_img")
    logo = models.ImageField(upload_to="profile_logo", null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(choices=City.CITY_LIST, max_length=50,
                            null=True, blank=True, default=City.ANY)
    address = models.CharField(max_length=300, null=True, blank=True)
    subscribed_to = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class ContactPhone(models.Model):
    TELEGRAM = 1
    VIBER = 2
    SOCIAL_CHOICES = ((1, 'Telegram'),
                      (2, 'Viber'))
    social = models.CharField(max_length=2,
                              choices=SOCIAL_CHOICES)
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name="contact_phone")
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.social} - {self.phone}"


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
