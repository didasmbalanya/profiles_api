from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializers a name for testing our API view"""

    name = serializers.CharField(max_length=10)


class UserProfileSerialzer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
