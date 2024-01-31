from rest_framework import viewsets, permissions
from ..serializers.shopping_cart_serializer import ShoppingCartSerializer
from ..models.shopping_cart import ShoppingCart


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Set the user to the current user if authenticated, otherwise leave it as None
        serializer.save(user=self.request.user if not self.request.user.is_anonymous else None)
