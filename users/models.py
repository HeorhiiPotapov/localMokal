from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Category
from django.core.validators import FileExtensionValidator


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
    logo = models.FileField(upload_to="profile_logo", null=True, blank=True,
                            validators=[FileExtensionValidator(['svg'])])
    brand = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    subscribed_to = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


# create phone for profile with
# <profile.phone.create(social=0, phone="+1...")>
class Phone(models.Model):
    PRIMARY = 0
    TELEGRAM = 1
    VIBER = 2
    WHATSUP = 3
    FACEBOOK = 4
    SOCIAL_CHOICES = [
        (0, 'Primary'),
        (1, 'Telegram'),
        (2, 'Viber'),
        (3, 'Whatsup'),
        (4, 'Facebook')
    ]
    social = models.CharField(max_length=2, choices=SOCIAL_CHOICES,
                              default=PRIMARY)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name="phone")
    phone = models.CharField(unique=True, max_length=13)

    def __str__(self):
        return f"{self.social} - {self.phone}"


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
