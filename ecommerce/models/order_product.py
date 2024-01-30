   
from django.db import models
from ecommerce.models.product import Product
from ecommerce.models.order import Order

 

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()