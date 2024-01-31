from datetime import timedelta
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
# from ecommerce.serializers.token_serializer import TokenSerializer
from ecommerce.utils.security import create_access_token  # Your token creation utility
from rest_framework import status, views
from rest_framework.response import Response
from ecommerce.serializers.user_serializer import UserCreateSerializer, UserResponseSerializer
from ecommerce.models.user import User 
from ecommerce.models.verificaiton_token import  VerificationToken
from ecommerce.models.department import  Department
from ecommerce.utils.security import generate_verification_token, send_verification_email
from django.core.exceptions import ValidationError
from django.conf import settings
ACCESS_TOKEN_EXPIRE_MINUTES = 60
from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response
from ecommerce.models.department import Department
from ecommerce.serializers.user_serializer import UserCreateSerializer
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# class 
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def register_customer(request):
#     if request.method == 'POST':
#         serializer = UserCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             # Create a new customer but mark them as unverified
#             customer = serializer.save(is_verified=False)

#             # Send verification email
#             verification_token = str(customer.id)
#             verification_url = f"http://your-website.com/verify/{verification_token}/"
#             email_subject = "Verify Your Email"
#             email_message = render_to_string(
#                 'verification_email.html',
#                 {'verification_url': verification_url}
#             )
#             email = EmailMessage(
#                 email_subject,
#                 email_message,
#                 to=[customer.email]
#             )
#             email.send()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterUserView(views.APIView):
    def post(self, request, *args, **kwargs):
        # Extract department_id from request data
        department_id = request.data.get('department_id')
        
        # Retrieve the Department instance or return a 404 Not Found response
        department = get_object_or_404(Department, id=department_id)
        
        # Include department in the data passed to the serializer
        request.data['department'] = department.id
        
        # Initialize the serializer with the request data
        serializer = UserCreateSerializer(data=request.data)
        
        # Validate and save the serializer
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # Return a success response
            return Response({'message': 'User registered successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Incorrect username or password')

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        token_data = {"access_token": access_token, "token_type": "Bearer"}
        return Response(token_data, status=status.HTTP_200_OK)


class CreateUserView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = generate_verification_token()
        verification_link = f"{settings.BASE_URL}/users/verify?token={token}"
        send_verification_email(user.email, verification_link)
        VerificationToken.objects.create(user=user, token=token)
        return Response(UserResponseSerializer(user).data, status=status.HTTP_201_CREATED)

class VerifyUserView(views.APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            verification_token = VerificationToken.objects.get(token=token)
            user = verification_token.user
            user.is_active = True
            user.save()
            verification_token.delete()
            return Response({'message': f'Email {user.email} verified successfully'}, status=status.HTTP_200_OK)
        except VerificationToken.DoesNotExist:
            raise ValidationError('Invalid verification token')

# class RegisterUserView(views.APIView):
#     def post(self, request, *args, **kwargs):
#         department_id = request.data.get('department_id')
#         try:
#             department = Department.objects.get(id=department_id)
#         except Department.DoesNotExist:
#             raise ValidationError('Department not found')
#         serializer = UserCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save(department=department)
#         return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)