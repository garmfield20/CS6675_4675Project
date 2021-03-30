from django.db import models

# Create your models here.
# change models
# run python manage.py makemigrations
# run python manage.py migrate

class distributors(models.Model):
    # name, password? address, last_update, registration_data, updates_count
    name = models.CharField(max_length=256)
    store_id = models.CharField(max_length=256)
    last_update = models.DateTimeField()
    registration_date = models.DateTimeField()
    update_count = models.IntegerField(default=0)

    def __str__(self):
        pass

class address(models.Model):
    store_id = models.ForeignKey(distributors, on_delete=models.CASCADE)
    address_line = models.CharField(max_length=256)
    zip_code = models.CharField(default="30332", max_length=12)
    city = models.CharField(default="Atlanta", max_length=256)
    state = models.CharField(default="Georgia", max_length=256)
    country = models.CharField(default="US", max_length=256)

    def __str__(self):
        pass
