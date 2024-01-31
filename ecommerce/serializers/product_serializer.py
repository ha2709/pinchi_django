# myapp/serializers/product_serializer.py
from rest_framework import serializers
from ecommerce.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'department', 'discount', 'category']
