from django.contrib import admin
from .models import Account, Patient, Distributor, Physician, Appointment, Vaccine

# Register your models here.
admin.site.register(Account)
admin.site.register(Patient)
admin.site.register(Distributor)
admin.site.register(Physician)
admin.site.register(Appointment)
admin.site.register(Vaccine)