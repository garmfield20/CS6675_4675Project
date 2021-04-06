from django.db import models

# Create your models here.

class user(models.Model):
  username = models.CharField(max_length=256)
  password = models.CharField(max_length=256)
  first_name = models.CharField(max_length=256)
  last_name = models.CharField(max_length=256)
  age = models.IntegerField(default=0)
  # char list with max of 100 pre-existing conditions in the list
  preexisting = models.CharField(max_length=256)
  occupation = models.CharField(max_length=256)
  living_situation = models.CharField(max_length=256)
  priority = models.CharField(default="low", max_length=256)

  def __str__(self):
    return self.username