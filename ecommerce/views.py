from django.shortcuts import render

from rest_framework import viewsets,  permissions
from ecommerce.models.user import User
from ecommerce.models.category import Category
from ecommerce.models.product import Product
from ecommerce.models.order import Order
from ecommerce.models.discount import Discount
from ecommerce.models.shopping_cart import ShoppingCart
# from .serializers import UserSerializer, CategorySerializer, ProductSerializer, OrderSerializer, DiscountSerializer, ShoppingCartSerializer
from rest_framework import status
from rest_framework.response import Response


 