from django.db import models
from ecommerce.models.category import Category

class Discount(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    objects = models.Manager()  # Explicitly define a manager