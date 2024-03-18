from inspect import FullArgSpec
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# We want to have 3 diferent types of Users,
# Customer
#  --  Data:
#    -- Name
#    -- Email
#    -- Phone
#    -- Address
#    -- Password
#    -- Profile Picture
#    -- Date of Birth.
#    -- National Verification Number or Ghana Card Number
# CustomerSupport - Admin with limited access and sepearte dashboard
# Admin - AccountManagers


class ProfileManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().select_related("user")


class User(AbstractUser):
    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "email"

    objects = models.Manager()
    profile = ProfileManager()


class UserProfile(models.Model):
    """
    Extends django `User` model with additional fields for a given user.
    """

    class UserType(models.TextChoices):
        CUSTOMER = "Customer"
        CUSTOMER_SUPPORT = "Customer Support"
        ADMIN = "Admin"

    user = models.OneToOneField(
        "User", on_delete=models.CASCADE, related_name="profile"
    )

    phone_number = models.CharField(
        max_length=20, blank=True, null=True, help_text=_("Phone number of the user")
    )
    profile_picture = models.ImageField(
        upload_to="profile_pictures",
        blank=True,
        null=True,
        help_text=_("Profile picture"),
    )
    date_of_birth = models.DateField(
        _("Date of Birth"),
        blank=True,
        null=True,
        help_text="Date of birth as given on your government-issued identification card",
    )
    national_verification_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text=_(
            "National Verification Number provided on your government-issued identification card"
        ),
    )
    bank_verification_number = models.CharField(
        _("Bank Verification Number"),
        max_length=20,
        null=False,
        blank=False,
        help_text=_("Bank Verification Number provided by your bank"),
    )
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.CUSTOMER,
    )
    last_login = models.DateTimeField(
        auto_now=True, help_text=_("Last known login time of this user")
    )
    verification_document = models.FileField(
        upload_to="verification_documents",
        blank=True,
        null=True,
        help_text=_("Document to verify the user"),
    )

    def full_name(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self) -> str:
        return f"{self.full_name()} - {self.user_type}"
