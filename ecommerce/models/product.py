from django.db import models
from ecommerce.models.category import Category
from ecommerce.models.department import Department
from ecommerce.models.discount import Discount
from ecommerce.models.product_category import ProductCategory
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='products')
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    objects = models.Manager()  # Explicitly define a manager
    
    def __str__(self):
        return self.name
  