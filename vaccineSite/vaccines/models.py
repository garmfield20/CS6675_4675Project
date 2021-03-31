from django.db import models

# Create your models here.

class vaccine(models.Model):
    vaccine_id = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)
    dose_required = models.IntegerField(default=2)
    if_used = models.BooleanField(default=False)
    expiration_date = models.DateField()
