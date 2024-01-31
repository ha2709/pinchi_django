from rest_framework import serializers
from ..models.product_category import ProductCategory
from .product_serializer import ProductSerializer
from .discount_serializer import DiscountSerializer

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'department']


class ProductCategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    discounts = DiscountSerializer(many=True, read_only=True)

    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'department', 'products', 'discounts']