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
            'sexe',
            'birthday',
            'password',
        )
def create(self, validated_data):
    return Comment.objects.create(**validated_data)