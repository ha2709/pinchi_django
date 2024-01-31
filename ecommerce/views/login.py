from datetime import timedelta
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
# from ecommerce.serializers.token_serializer import TokenSerializer
from ecommerce.utils.security import create_access_token  # Your token creation utility

ACCESS_TOKEN_EXPIRE_MINUTES = 60

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

class RegisterUserView(views.APIView):
    def post(self, request, *args, **kwargs):
        department_id = request.data.get('department_id')
        try:
            department = Department.objects.get(id=department_id)
        except Department.DoesNotExist:
            raise ValidationError('Department not found')
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(department=department)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)