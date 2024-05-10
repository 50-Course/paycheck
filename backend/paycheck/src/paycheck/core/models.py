from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField
from uuid import uuid4


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
        - a user profile that contains the user bio and additional metadata,
        - a `user` model that contains the customer information, essentially the end-users of our system
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

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    USERNAME_FIELD = "email"

    class Meta:
        abstract = True

    def __str__(self):
        return self.username

    @property
    def full_name(self) -> str:
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    @property
    def is_verified(self) -> bool:
        # TODO: Implement this
        return NotImplementedError
