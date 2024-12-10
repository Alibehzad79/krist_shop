from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name=_("Email"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class UserProfile(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.DO_NOTHING,
        related_name="profile",
        verbose_name=_("User"),
    )
    first_name = models.CharField(max_length=50, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=50, verbose_name=_("Last Name"))
    phone_number = models.CharField(
        max_length=50, verbose_name=_("Phone Number"), unique=True
    )

    profile_image = models.ImageField(
        upload_to="profiles/images/", verbose_name=_("Profile Image")
    )
    profile_bg_image = models.ImageField(
        upload_to="profiles/images/", verbose_name=_("Profile Background Image")
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Address(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name=_("Prifle"),
        related_name="addresses",
    )
    phone_number = models.CharField(max_length=50, verbose_name=_("Phone Number"))
    country = models.CharField(max_length=50, verbose_name=_("Country"))
    city = models.CharField(max_length=50, verbose_name=_("City"))
    state = models.CharField(max_length=100, verbose_name=_("State"))
    zip_code = models.CharField(max_length=50, verbose_name=_("Zip Code"))
    more_info = models.TextField(verbose_name=_("More Info"))

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return self.city
