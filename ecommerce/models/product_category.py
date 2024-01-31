from django.db import models
import uuid

class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='product_categories')

    def __str__(self):
        return self.name
