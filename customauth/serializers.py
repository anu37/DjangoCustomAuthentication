from rest_framework import serializers
from rest_framework import viewsets
from .models import (
    AuthToken,
    Application,
)

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

    def create(self, validated_data):
        application = Application(**validated_data)
        application.save()
        return application


class AuthTokenCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthToken
        fields = "__all__"

    def create(self, validated_data):
        authtoken = AuthToken(**validated_data)
        authtoken.save()
        return authtoken