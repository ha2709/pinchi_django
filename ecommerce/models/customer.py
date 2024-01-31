from django.db import models
import uuid

# from ecommerce.models.user import User
from ecommerce.models.customer_category import CustomerCategory
 
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    successful_orders = models.IntegerField(default=0)

    # Change the OneToOneField to use a string reference
    user = models.OneToOneField('ecommerce.User', on_delete=models.CASCADE, related_name='customer')


    def categorize(self):
        if 0 <= self.successful_orders <= 20:
            return CustomerCategory.BRONZE
        elif 20 < self.successful_orders <= 50:
            return CustomerCategory.SILVER
        else:
            return CustomerCategory.GOLD