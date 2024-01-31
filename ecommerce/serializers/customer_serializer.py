from rest_framework import serializers
from ecommerce.models.customer import Customer

class CustomerSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'email', 'successful_orders', 'category']

    def get_category(self, obj):
        return obj.categorize().value
