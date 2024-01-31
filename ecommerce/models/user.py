
from django.db import models
import uuid
from ecommerce.models.customer import Customer
from ecommerce.models.department import Department

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    hashed_password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='users')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.email
