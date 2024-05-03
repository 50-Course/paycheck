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
    first_name = models.CharField(
        _("First Name"),
        help_text="Given name of the user",
        max_length=40,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        _("Last Name"),
        help_text="Surname of the user",
        max_length=40,
        blank=False,
        null=False,
    )

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
        return f"{self.user}"

    def __str__(self) -> str:
        return f"{self.full_name()} - {self.user_type}"


class SupportUser(models.Model):
    """
    Represent a member of the support team.

    SupportUser is someone who is an admin with limited access to the system

    They can:
        - Manage disputes and resolutions on behalf of the user
        - Manage user accounts
    """

    user = models.OneToOneField(
        _("Support"),
        on_delete=models.CASCADE,
        related_name="support_user",
        help_text=_("Support User"),
    )


class AdminUser(models.Model):
    """
    Represent an admin user.

    AdminUser is someone who is an admin with full access to the system

    They can:
        - Manage disputes and resolutions on behalf of the user
        - Manage user accounts -blacklist or whitelist a user
        - Manage user support staff
        - Manage user support staff accounts
        - Manage user support staff permissions
    """

    user = models.OneToOneField(
        _("Admin User"),
        on_delete=models.CASCADE,
        related_name="admin_user",
        help_text=_("Admin User"),
    )
