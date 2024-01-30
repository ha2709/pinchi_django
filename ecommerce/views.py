from django.shortcuts import render

from rest_framework import viewsets,  permissions
from ecommerce.models.user import User
from ecommerce.models.category import Category
from ecommerce.models.product import Product
from ecommerce.models.order import Order
from ecommerce.models.discount import Discount
from ecommerce.models.shopping_cart import ShoppingCart
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, OrderSerializer, DiscountSerializer, ShoppingCartSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
def register_user(request):
    # This is a simple example. You should add more validation and error checking.
    user = User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['password']
    )
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Set the user to the current user if authenticated, otherwise leave it as None
        serializer.save(user=self.request.user if not self.request.user.is_anonymous else None)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def perform_create(self, serializer):
        # Orders can only be created by authenticated users
        serializer.save(user=self.request.user)

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

