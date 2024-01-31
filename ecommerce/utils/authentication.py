import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from ecommerce.models.user import User  # Assuming you have a User model
from django.contrib.auth.models import AnonymousUser

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            user_email = payload.get('sub')
            if user_email is None:
                raise exceptions.AuthenticationFailed('Invalid JWT token')
            
            try:
                user = User.objects.get(email=user_email)
            except User.DoesNotExist:
                raise exceptions.AuthenticationFailed('No such user')
            
            return (user, None)

        except jwt.PyJWTError:
            raise exceptions.AuthenticationFailed('Invalid JWT token')
