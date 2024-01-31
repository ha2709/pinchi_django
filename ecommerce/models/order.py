from django.db import models
import uuid
 
from ecommerce.models.customer import Customer
class Order(models.Model):
 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product)
    status = models.CharField(max_length=255, null=True)
    total_price = models.FloatField()
    # customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()  # Explicitly define a manager
    def __str__(self):
        return f"Order {self.id} - Status: {self.status}"
     