from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField
from uuid import uuid4
from django.conf import settings


class BaseUser(AbstractUser):
    """
    Represent an abstract user model.

    This is a custom user model that extends the Django's AbstractUser model, and is not meant
    to be used directly. It is used to create a custom user model that can be used in the Django
    project. The custom user model is created by extending the AbstractUser model and adding
    additional fields to it. The custom user model can be used to store additional information

    For users in our system, please see the internal documentation, as it contains the
    information about the user types in our system.

    We have:
        - a user that contains the user basic information, needed by django auth system
        - a `user_profile` model that contains the customer information, essentially the end-users of our system
        - a `Support` model that contains the support information, essentially the support staff of our system
        - a `Admin` model that contains the admin information, essentially the admin staff of our system

    AS SUCH, THIS IS AN ABSTRACT CLASS AND NOT MENT TO BE USED DIRECTLY. PLEASE CONSULT WITH LEAD OR PROJECT MAINTAINER
    BEFORE TOUCHING THIS MODEL.


    Attributes:
        username: A string representing the username.
        email: A string representing the email.
        first_name: A string representing the first name.
        last_name: A string representing the last name.
        is_active: A boolean representing the active status.
        is_staff: A boolean representing the staff status.
        date_joined: A datetime representing the date joined.
        last_login: A datetime representing the last login.
        phone_number: A string representing the phone number.

    """

    cannoical_id = models.UUIDField(
        _("user id"),
        primary_key=True,
        default=uuid4,
        editable=False,
        help_text=(
            "This is a unique identifier for the user",
            "It is generated automatically when a new user is created and cannot be changed",
        ),
    )
    first_name = models.CharField(
        _("first name"),
        max_length=30,
        blank=True,
        help_text="Designates the first name of the user",
    )
    middle_name = models.CharField(
        _("middle name"),
        max_length=30,
        blank=True,
        null=True,
        help_text="Designates the middle name of the user",
    )
    last_name = models.CharField(
        _("last name"),
        max_length=30,
        blank=True,
        help_text="Designates the last name of the user",
    )
    last_login = models.DateTimeField(
        _("last login"),
        blank=True,
        null=True,
        help_text="Designates the last login of the user",
    )

    email = models.EmailField(
        _("email address"), unique=True, help_text="Designates the email of the user"
    )
    phone_number = PhoneField(
        _("phone number"),
        blank=True,
        null=True,
        help_text="Designates the phone number of the user",
    )

    is_customer = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username

    @property
    def full_name(self) -> str:
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email

        if kwargs.get("is_customer") is None:
            self.is_customer = True

        profile = UserProfile(user=self).save()
        kwargs["profile"] = profile
        super().save(*args, **kwargs)


class Address(models.Model):
    """
    Represent an address location. This helps in storing the location of the user, as well as
    during analytical session for internal teams, e.g filtering all users by location.

    """

    address_line_1 = models.CharField(
        _("address line 1"),
        max_length=100,
        blank=True,
        help_text="Designates the address line 1 of the user",
    )
    address_line_2 = models.CharField(
        _("address line 2"),
        max_length=100,
        blank=True,
        help_text="Designates the address line 2 of the user",
    )
    city = models.CharField(
        _("city"),
        max_length=100,
        blank=True,
        help_text="Designates the city of the user",
    )
    state = models.CharField(
        _("state"),
        max_length=100,
        blank=True,
        help_text="Designates the state of the user",
    )
    country = models.CharField(
        _("country"),
        max_length=100,
        blank=True,
        help_text="Designates the country of the user",
    )
    zip_code = models.CharField(
        _("zip code"),
        max_length=100,
        blank=True,
        help_text="Designates the zip code of the user",
    )


class UserProfile(models.Model):
    """
    Represent a user model.
    """

    class VerificationStatus(models.TextChoices):
        PENDING = "PENDING", _("PENDING")
        VERIFIED = "VERIFIED", _("VERIFIED")
        REJECTED = "REJECTED", _("REJECTED")

    verfication_id_type = [
        ("NIN", "NIN"),  # Nigerian Identity Number
        ("BVN", "BVN"),  # Bank Verification Number of the user
        ("DRIVER_LICENSE", "DRIVER_LICENSE"),
        ("VOTER_CARD", "VOTER_CARD"),
        ("INTERNATIONAL_PASSPORT", "INTERNATIONAL_PASSPORT"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    occupation = models.CharField(
        _("occupation"),
        max_length=100,
        blank=True,
        help_text=(
            "User occupation allows us to know the type of user",
            "It is used for loan disbursement, and analytical purposes",
        ),
    )
    birth_date = models.DateField(
        _("birth date"),
        blank=True,
        null=True,
        help_text="Designates the date of birth of the user",
    )
    profile_picture = models.ImageField(
        _("profile picture"),
        upload_to="profile_pictures/",
        blank=True,
        null=True,
        help_text=(
            "Stores the selfies of the user at KYC process",
            "Selfies is stored in the `profile_pictures` directory",
        ),
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        help_text="Designates the address of the user",
        null=True,
    )
    verification_status = models.CharField(
        _("verification status"),
        max_length=10,
        choices=VerificationStatus.choices,
        default=VerificationStatus.PENDING,
        help_text="Desiginates if this useer has been verified to access our system",
    )
    verification_number = models.CharField(
        _("verification number"),
        max_length=40,
        blank=True,
        help_text="Designates the governent-issued identity number of the user, e.g NIN, BVN, etc.",
    )
    verification_id = models.ImageField(
        _("verification id"),
        upload_to="verification_ids/",
        blank=True,
        null=True,
        help_text=(
            "Stores the government-issued verification id of the user",
            "Verification id is stored in the `verification_ids` directory",
        ),
    )

    class Meta:
        verbose_name = _("user_profile")
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["verification_status"]),
            models.Index(fields=["verification_number"]),
        ]

    def __str__(self):
        return self.user.full_name()

    @property
    def is_verified(self):
        return self.verification_status

    @is_verified.setter
    def is_verified(self, value: str) -> None:
        self.verification_status = value


class Customer(BaseUser):
    """
    A proxy model that represents a customer.

    Helps abstracting away the `BaseUser` model and provide, initutive way to access
    and work with the model.

    Usage:

        customer = Customer.objects.get(email="email@email.com")
        print(customer.full_name)

        customer = Customer(**fields, **kwargs)
        customer.save() # overrides the user.save() method

    """

    class Meta:
        proxy = True


class Support(BaseUser):
    """
    A support user is essentially, the a member of the customer support team,
    they can adminster and manage support tickets
    """

    class Meta:
        proxy = True

    def __str__(self):
        return self.user.full_name()


class Admin(BaseUser):
    class Meta:
        proxy = True

    def __str__(self):
        return self.user.full_name()
