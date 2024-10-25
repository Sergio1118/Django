from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser

class InputSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    birthDate = serializers.DateField(source="birth_date")
    biography = serializers.CharField(required=False)

    class Meta:
        abstract = True


class OutputSerializer(InputSerializer):
    password = None
    accessToken = serializers.CharField(source="access_token")
    refreshToken = serializers.CharField(source="refresh_token")
  