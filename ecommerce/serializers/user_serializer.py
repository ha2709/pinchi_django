# myapp/serializers/user_serializer.py
from rest_framework import serializers
from ecommerce.models.user import User
from django.contrib.auth.hashers import make_password

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'   