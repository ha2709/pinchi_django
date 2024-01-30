from django.db import models
from ecommerce.models.user import User
from ecommerce.models.product import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()  # Explicitly define a manager