from django.db import models
from .order import Order
class OrderItem(models.Model):
    # other fields...
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
