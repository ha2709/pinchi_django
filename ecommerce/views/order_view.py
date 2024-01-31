from rest_framework import viewsets, permissions
from ..models.order import Order
from ..serializers.order_serializer import OrderSerializer



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def perform_create(self, serializer):
        # Orders can only be created by authenticated users
        serializer.save(user=self.request.user)
