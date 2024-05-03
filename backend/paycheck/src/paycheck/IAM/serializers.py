from .models import SupportUser, Adminuser, Customer, UserProfile, UserProofile, User
from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel - get_user_model()


class UserSerializer(serializers.Serializer):
    """
    User serializers is the base serializer for all user types

    It provides the barest important information that is allowed to be shared
    """

    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)
    email_address = serializers.EmailField()
    phone_number = serializers.CharField(max_length=20)

    class Meta:
        model = User
        exclude = [
            "password",
            "is_staff",
            "is_superuser",
            "is_active",
            "date_joined",
            "last_login",
            "groups",
            "user_permissions",
        ]
        read_only_fields = ["id"]


class CustomerSerializer(serializers.Serializer):
    """
    Customer serializer provides the information about the customer that is allowed to be shared over
    API contracts and integrations
    """

    user = UserSerializer()
    date_of_birth = serializers.DateField()
    photo_id = serializers.ImageField()

    full_name = serializers.SerializerMethodField()

    def get_full_name(self) -> str:
        pass

    class Meta:
        model = Customer
        fields = ["user", "date_of_birth", "photo_id"]
        exclude = ["user", "bvn", "nin"]


class SupportUserSerializer(serializers.ModelSerializer):
    """
    Shares the information regarding a member of our internal platform from the support team
    that can moderate or interact with a user
    """

    class Meta:
        model = SupportUser


class AdminSerializer(serializers.ModelSerializer):
    """
    Shares the information regarding a member of our internal platform from the admin team
    that can manage a user or anyone on the platform
    """

    class Meta:
        model = Adminuser


class UserProfileWriteSerializer(serializers.Serializer):
    """
    Defines the information that can be written to the user profile
    """

    user = UserSerializer()

    def create(self, *args, **kwargs) -> None:
        pass

    def update(self, instance, validated_data):
        self.user = UserModel.objects.get(id=validated_data.get("user").get("id"))
