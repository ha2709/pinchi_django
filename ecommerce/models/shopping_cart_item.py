from django.db import models
import uuid

class ShoppingCartItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField()
    shopping_cart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"CartItem {self.id} - Quantity: {self.quantity}"
