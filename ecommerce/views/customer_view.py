from rest_framework.views import APIView
from rest_framework.response import Response
from ecommerce.models.customer import Customer
from ecommerce.serializers.customer_serializer import CustomerSerializer

class CustomerList(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)