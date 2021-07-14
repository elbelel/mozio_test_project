from django.db import models
from provider.models import Provider


# Create your models here.

class Polygon(models.Model):
    name = models.CharField(max_length=255)
    provider = models.OneToOneField(Provider,default=None, on_delete=models.CASCADE)
    price = models.IntegerField()
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)

    def __str__(self):
        return self.name
