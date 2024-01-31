from rest_framework import serializers
from ..models.shopping_cart_item import ShoppingCartItem

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItem
        fields = ['id', 'product', 'quantity', 'shopping_cart']
