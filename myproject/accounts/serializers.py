from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Client
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            return user
        raise serializers.ValidationError('Incorrect Credentials')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = ('username', 'email', 'password', 'password_confirmation', 'country', 'phone_code', 'phone_number', 'organization', 'bio')

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return data

    def create(self, validated_data):
        user = Client.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            country=validated_data['country'],
            phone_code=validated_data['phone_code'],
            phone_number=validated_data['phone_number'],
            organization=validated_data['organization'],
            bio=validated_data['bio']
        )
        return user
