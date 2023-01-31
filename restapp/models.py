from django.db import models

# Create your models here.
class Course(models.Model):
    Name: models.CharField(max_length=200, blank=False, default='')
    Description: models.CharField(max_length=200, blank=False, default='')
    Published: models.BooleanField(default=False)