from django.db import models

class Token(models.Model):
    access_token = models.CharField(max_length=255)
    token_type = models.CharField(max_length=20)

    def __str__(self):
        return self.access_token
