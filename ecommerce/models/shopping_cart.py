from django.db import models
from django.conf import settings
# from ecommerce.models.product import Product
 
import uuid

class ShoppingCart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Assuming Product model exists
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='shopping_carts')
    objects = models.Manager()  # Explicitly define a manager
    def __str__(self):
        return f"ShoppingCart {self.id}"
