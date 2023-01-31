from django.db import models
from statistics import mode


# Create your models here.
class employee(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Password=models.CharField(max_length=200)

    def __str__(self):
        return self.Name
