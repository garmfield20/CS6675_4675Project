from django.db import models
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'physicians')))
sys.path.append(os.path.abspath(os.path.join('..', 'user')))
from physicians.models import physician
from user.models import user


# Create your models here.
class appointments(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    currphysician = models.ForeignKey(physician, on_delete = models.CASCADE)
    patient = models.ForeignKey(user, on_delete = models.CASCADE)
    vaccineName = models.CharField(default = "Pfizer", max_length=256)
    dose = models.IntegerField(default = 1)

    #whats the identifier here?
