from rest_framework import serializers
from ecommerce.models.user import User
from ecommerce.models.category import Category
from ecommerce.models.product import Product
from ecommerce.models.order import Order
from ecommerce.models.discount import Discount
from ecommerce.models.shopping_cart import ShoppingCart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'department']
 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    product_category_name = serializers.ReadOnlyField(source='product_category.name')

    class Meta:
        model = Discount
        fields = ['id', 'product_category', 'product_category_name', 'discount_percentage']
         

class ShoppingCartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ['id', 'user', 'products']
 