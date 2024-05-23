from rest_framework import serializers
from django.conf import settings

User = settings.AUTH_USER_MODEL

from src.paycheck.core.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User


class UserProfileSerializer(serializers.ModelSerializer):
    user_data = UserSerializer()

    class Meta:
        model = UserProfile
        exclude = ("id",)


class WritableUserProfileSerializer(serializers.Serializer):
    """
    This serializer is used to create or update a user profile.


    Do not use this serializer in READ operation contexts for retrieving
    user information as it may display sensitive information.

    """

    user_data = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop("user_data")
        user = User.objects.create(**user_data)
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user_data")
        user = instance.user
        user.username = user_data.get("username", user.username)
        user.email = user_data.get("email", user.email)
        user.save()
        instance.__dict__.update(**validated_data)
        instance.save()
        return instance
