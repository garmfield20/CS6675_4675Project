from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

preexistingChoices = ((1, "Cancer"), (2, "Cerebrovascular disease"), (3, "Chronic kidney disease"), 
(4, "COPD"), (5, "Diabetes mellitus, type 1"), (6, "Diabetes mellitus, type 2"), (7, "Heart conditions"),
 (8, "Smoking"), (9, "Obesity"), (10, "Pregnancy"), (11, "Down syndrome"), (12, "HIV"), 
 (13, "Neurologic conditions"), (14, "Overweight"), (15, "Lung disease"), (16, "Sickle cell disease"), 
 (17, "Solid organ or blood stem cell transplantation"), (18, "Substance use disorders"), 
 (19, "Cystic fibrosis"), (20, "Neurologic conditions"), (21, "Thalassemia"), (22, "Asthma"), 
 (23, "Hypertension"), (24, "Liver disease"), (25, "Immune Deficiencies"))

occupationChoices = ((1, "Agriculture"), (2, "Clothing Industry"), (3, "Computer Science/ IT"), 
(4, "Construction"), (5, "Education"), (6, "Entertainment"), (7, "Finance/ Accounting"), (8, "First Responder"), 
(9, "Food Services"), (10, "Government Employee"), (11, "Law"), (12, "Medical Field"),
 (13, "Military"), (14, "Other (In-person)"), (15, "Other (Virtual)"))
  
livingChoices = ((1, "Independent (1 person)"), (2, "Small Group (2-6)"), 
(3, "Small Group Housing (7 - 20)"), (4, "Large Group Housing (21+)"), 
(5, "Assisted Living"), (6, "Live with someone that is at risk"))

class user(models.Model):
  username = models.CharField(max_length=256, primary_key = True)
  password = models.CharField(max_length=256)
  first_name = models.CharField(max_length=256)
  last_name = models.CharField(max_length=256)
  age = models.IntegerField(default=0)
  preexisting = MultiSelectField(choices = preexistingChoices, default = None)
  # check box list of occupations
  occupation = MultiSelectField(choices = occupationChoices, default = None)
  #check box list of living situations
  living_situation = MultiSelectField(choices = livingChoices, default = None)

  # make this based on prexisting, occupation, and living situation
  # red flags
  #options: low, medium, high

  priority = models.CharField(max_length=256)

  def __str__(self):
    return self.username

