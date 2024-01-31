from django.db import models
import uuid

class Department(models.Model):
    # Assuming the Department model has at least an ID field
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
