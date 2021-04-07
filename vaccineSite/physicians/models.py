from django.db import models
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'distributors')))
from distributors.models import distributors

# Create your models here.

class physicians(models.Model):
    username = models.CharField(max_length=256, primary_key=True)
    first_name = models.CharField(max_length=256, default = None)
    last_name = models.CharField(max_length=256, default = None)
    distributor = models.ForeignKey(distributors, on_delete=models.RESTRICT)

    #list appointments by physician?



    def __str__(self):
        return self.username
