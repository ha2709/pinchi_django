# myapp/views.py
from rest_framework import viewsets
from ecommerce.models.user import User  
from ecommerce.serializers.user_serializer import UserSerializer 
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

@api_view(['POST'])
def register_user(request):
     
    user = User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['password']
    )
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
 
