from django.db import models
import uuid

from ecommerce.models.user import User
from ecommerce.models.customer_category import CustomerCategory
 
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    successful_orders = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')

    def categorize(self):
        if 0 <= self.successful_orders <= OrderThreshold.TWENTY:
            return CustomerCategory.BRONZE
        elif OrderThreshold.TWENTY < self.successful_orders <= OrderThreshold.FIFTY:
            return CustomerCategory.SILVER
        else:
            return CustomerCategory.GOLD