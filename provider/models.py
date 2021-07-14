from django.db import models

# Create your models here.

class Provider(models.Model):
    email = models.EmailField(unique=True, error_messages={'unique': 'A user with this email already exist'})
    name = models.CharField(max_length=255)
    phone_number = models.TextField(max_length=255)
    language = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)

    def __str__(self):
        return self.name