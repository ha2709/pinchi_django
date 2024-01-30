from django.db import models
from django.conf import settings
from ecommerce.models.product import Product

class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, through='ShoppingCartProduct')

    objects = models.Manager()  # Explicitly define a manager