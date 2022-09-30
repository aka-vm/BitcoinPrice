from django.db import models

# Create your models here.
class Bitcoin(models.Model):
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Bitcoin Price: {self.price} at {self.timestamp}"