from django.db import models
from multiselectfield import MultiSelectField

# authentication
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe

preexistingChoices = ((1, "Cancer"), (2, "Cerebrovascular disease"), (3, "Chronic kidney disease"),
                      (4, "COPD"), (5, "Diabetes mellitus, type 1"), (6, "Diabetes mellitus, type 2"),
                      (7, "Heart conditions"),
                      (8, "Smoking"), (9, "Obesity"), (10, "Pregnancy"), (11, "Down syndrome"), (12, "HIV"),
                      (13, "Neurologic conditions"), (14, "Overweight"), (15, "Lung disease"),
                      (16, "Sickle cell disease"),
                      (17, "Solid organ or blood stem cell transplantation"), (18, "Substance use disorders"),
                      (19, "Cystic fibrosis"), (20, "Neurologic conditions"), (21, "Thalassemia"), (22, "Asthma"),
                      (23, "Hypertension"), (24, "Liver disease"), (25, "Immune Deficiencies"))

occupationChoices = ((1, "Agriculture"), (2, "Clothing Industry"), (3, "Computer Science/ IT"),
                     (4, "Construction"), (5, "Education"), (6, "Entertainment"), (7, "Finance/ Accounting"),
                     (8, "First Responder"),
                     (9, "Food Services"), (10, "Government Employee"), (11, "Law"), (12, "Medical Field"),
                     (13, "Military"), (14, "Other (In-person)"), (15, "Other (Virtual)"))

livingChoices = ((1, "Independent (1 person)"), (2, "Small Group (2-6)"),
                 (3, "Small Group Housing (7 - 20)"), (4, "Large Group Housing (21+)"),
                 (5, "Assisted Living"), (6, "Live with someone that is at risk"))

priorityChoices = (('low', 'low'), ('medium', 'medium'), ('high', 'high'))


class Account(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_physician = models.BooleanField(default=False)
    is_distributor = models.BooleanField(default=False)

    address_line = models.CharField(default="842 Peachtree St NE",max_length=256)
    zip_code = models.CharField(default="30308", max_length=12)
    city = models.CharField(default="Atlanta", max_length=256)
    state = models.CharField(default="Georgia", max_length=256)
    country = models.CharField(default="US", max_length=256)


class Patient(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(default=0)
    preexisting = MultiSelectField(choices=preexistingChoices, default=None)
    # check box list of occupations
    occupation = MultiSelectField(choices=occupationChoices, default=None)
    # check box list of living situations
    living_situation = MultiSelectField(choices=livingChoices, default=None)

    # make this based on prexisting, occupation, and living situation
    # red flags
    # options: low, medium, high

    priority = models.CharField(choices=priorityChoices, default=None, max_length=256)

    def __str__(self):
        return self.user.username


class Distributor(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=256)
    last_update = models.DateField(default='2021-04-10')
    registration_date = models.DateField(default='2021-04-10')
    update_count = models.IntegerField(default=0)
    rating = models.FloatField(default=5)
    # physicians = models.ForeignKey(physicians, on_delete=models.RESTRICT)

    def __str__(self):
        return self.user.username


class Physician(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    currphysician = models.OneToOneField(Physician, on_delete=models.RESTRICT)
    patient = models.OneToOneField(Patient, on_delete=models.RESTRICT)
    vaccineName = models.CharField(default="Pfizer", max_length=256)
    dose = models.IntegerField(default=1)

    class Meta:
        unique_together = (('currphysician', 'patient'),)


class Vaccine(models.Model):
    vaccine_id = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)
    dose_required = models.IntegerField(default=2)
    if_used = models.BooleanField(default=False)
    expiration_date = models.DateField()
