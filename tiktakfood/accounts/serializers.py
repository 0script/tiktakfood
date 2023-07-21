from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'address',
            'password'
        )
    def create(self, validated_data):
        user=CustomUser.objects.create_user(validated_data)
        return user
