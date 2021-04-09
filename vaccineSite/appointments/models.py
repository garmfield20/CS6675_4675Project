from django.db import models
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'physicians')))
sys.path.append(os.path.abspath(os.path.join('..', 'user')))
from physicians.models import physician
from user.models import user


# Create your models here.
class appointment(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    currphysician = models.OneToOneField(physician, on_delete = models.RESTRICT)
    patient = models.OneToOneField(user, on_delete = models.RESTRICT)
    vaccineName = models.CharField(default = "Pfizer", max_length=256)
    dose = models.IntegerField(default = 1)

    #whats the unique indentifier- startTime and currphysician
