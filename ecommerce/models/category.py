from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    objects = models.Manager()  # Explicitly define a manager
    
    def __str__(self):
        return self.name
