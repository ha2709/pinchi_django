    
from django.db import models
from ecommerce.models.product import Product
from ecommerce.models.shopping_cart import ShoppingCart

 

class ShoppingCartProduct(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)