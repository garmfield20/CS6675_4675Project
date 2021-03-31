from django.db import models

# Create your models here.
# change models
# run python manage.py makemigrations
# run python manage.py migrate

class distributors(models.Model):
    # name, password? address, last_update, registration_data, updates_count
    distributor_id = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    last_update = models.DateField()
    registration_date = models.DateField()
    update_count = models.IntegerField(default=0)
    rating = models.FloatField()

    address_line = models.CharField(default="842 Peachtree St NE",max_length=256)
    zip_code = models.CharField(default="30308", max_length=12)
    city = models.CharField(default="Atlanta", max_length=256)
    state = models.CharField(default="Georgia", max_length=256)
    country = models.CharField(default="US", max_length=256)


