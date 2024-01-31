from rest_framework import serializers
from ..models.order import Order

class OrderItemSerializer(serializers.ModelSerializer):
    pass
    # Define fields and Meta class...

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'customer', 'order_items']
