# myapp/serializers/user_serializer.py
from rest_framework import serializers
from ecommerce.models.user import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from ..models.user import User
from ..models.department import Department

class UserCreateSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'department', ... )  # include other fields as necessary

    # Add create method if not present to handle saving of user with department
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'password')
        
#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             password=make_password(validated_data['password'])
#         )
#         user.save()
#         return user

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'   