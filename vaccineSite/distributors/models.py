from django.db import models
# import sys, os
# sys.path.append(os.path.abspath(os.path.join('..', 'physicians')))
# from physicians.models import physicians

# Create your models here.
# change models
# run python manage.py makemigrations
# run python manage.py migrate

class distributor(models.Model):
    # name, password? address, last_update, registration_data, updates_count
    distributor_id = models.CharField(max_length=256, primary_key = True)
    name = models.CharField(max_length=256)
    last_update = models.DateField()
    registration_date = models.DateField()
    update_count = models.IntegerField(default=0)
    rating = models.FloatField()
    # physicians = models.ForeignKey(physicians, on_delete=models.RESTRICT)

    address_line = models.CharField(default="842 Peachtree St NE",max_length=256)
    zip_code = models.CharField(default="30308", max_length=12)
    city = models.CharField(default="Atlanta", max_length=256)
    state = models.CharField(default="Georgia", max_length=256)
    country = models.CharField(default="US", max_length=256)

    def __str__(self):
        return self.distributor_id


