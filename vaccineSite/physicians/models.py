from django.db import models

# Create your models here.

class physician(models.Model):
    username = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
