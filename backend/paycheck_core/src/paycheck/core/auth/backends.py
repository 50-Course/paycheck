from django.contrib.auth.backends import BaseBackend


class PhoneEmailOrAccountNumberAuthBackend(BaseBackend):
    """
    Authenticates a user into the platform using the user's assigned
    unique account number, email address or phone number
    """

    def authenticate(self, request, username, password, *args, **kwargs):
        """
        Authenticate a user based on the username and password
        """
        pass
