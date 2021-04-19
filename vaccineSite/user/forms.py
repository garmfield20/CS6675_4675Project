from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import Account, Patient, Distributor, Physician, Vaccine, Appointment


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2', 'address_line', 'zip_code',
         'city', 'state', 'country']



class DistributorSignUpForm(UserCreationForm):

    registration_date = forms.DateField()
    # rating = forms.FloatField()

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['username', 'email', 'password1', 'password2', 'address_line', 'zip_code',
         'city', 'state', 'country']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_distributor = True
        if commit:
            user.save()

        
        distributor = Distributor.objects.create(user=user)
        distributor.registration_date = self.cleaned_data.get('registration_date')
        distributor.last_update = self.cleaned_data.get('registration_date')
        #distributor.rating = self.cleaned_data.get('rating')
        distributor.save()

        return user
    

class DistributorApptAddForm(forms.ModelForm):
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    physician = forms.ModelChoiceField(queryset = Physician.objects, required=False, blank=True)
    patient = forms.ModelChoiceField(queryset = Patient.objects, required=False, blank =True)
    vaccine_name = forms.ModelChoiceField(queryset = Vaccine.objects)
    dose = forms.IntegerField()

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(DistributorApptAddForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Appointment
        fields = ['start_time','end_time', 'physician','patient','vaccine_name', 'dose']

    def save(self, commit=True):
        appointment = Appointment()
        appointment.distributor = Distributor.objects.get(user=self.user)
        appointment.start_time = self.cleaned_data.get('start_time')
        appointment.end_time = self.cleaned_data.get('end_time')
        appointment.physician = self.cleaned_data.get('physician')
        appointment.patient = self.cleaned_data.get('patient')
        appointment.vaccine_name = self.cleaned_data.get('vaccine_name')
        appointment.dose = self.cleaned_data.get('dose')
        appointment.save()


class VaccineForm(forms.ModelForm):
    vaccine_id = forms.CharField(max_length=256)
    brand = forms.CharField(max_length=256)
    dose_required = forms.IntegerField()
    expiration_date = forms.DateField()
    
    class Meta:
        model = Vaccine
        fields = ['vaccine_id', 'brand', 'dose_required', 'expiration_date']

    def save(self, commit=True):
        vaccine = Vaccine()
        vaccine.vaccine_id = self.cleaned_data.get('vaccine_id')
        vaccine.brand = self.cleaned_data.get('brand')
        vaccine.dose_required = self.cleaned_data.get('dose_required')
        vaccine.if_used = self.cleaned_data.get('if_used')
        vaccine.expiration_date = self.cleaned_data.get('expiration_date')
        vaccine.save()


class PhysicianSignUpForm(UserCreationForm):
    distributor = forms.ModelChoiceField(queryset = Distributor.objects)

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name',
        'address_line', 'zip_code', 'city', 'state', 'country']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_physician = True
        if commit:
            user.save()
        physician = Physician(user=user)
        physician.distributor=self.cleaned_data.get('distributor')
        physician.save()

        return user

class PhysicianApptAddForm(forms.ModelForm):
    physician = forms.ModelChoiceField(queryset = Physician.objects, required=False, blank=True)
    class Meta:
        model = Appointment
        fields = ['physician']
    def save(self, commit=True):
        appointment = Appointment()
        appointment.physician = self.cleaned_data.get('physician')
        appointment.save()


class PatientSignUpForm(UserCreationForm):
    age = forms.IntegerField()

    preexistingChoices = ((1, "Cancer"), (2, "Cerebrovascular disease"), (3, "Chronic kidney disease"),
                          (4, "COPD"), (5, "Diabetes mellitus, type 1"), (6, "Diabetes mellitus, type 2"),
                          (7, "Heart conditions"),
                          (8, "Smoking"), (9, "Obesity"), (10, "Pregnancy"), (11, "Down syndrome"), (12, "HIV"),
                          (13, "Neurologic conditions"), (14, "Overweight"), (15, "Lung disease"),
                          (16, "Sickle cell disease"),
                          (17, "Solid organ or blood stem cell transplantation"), (18, "Substance use disorders"),
                          (19, "Cystic fibrosis"), (20, "Neurologic conditions"), (21, "Thalassemia"), (22, "Asthma"),
                          (23, "Hypertension"), (24, "Liver disease"), (25, "Immune Deficiencies"), (26, "None of the above"))
    preexisting = forms.MultipleChoiceField(
        choices=preexistingChoices,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    occupationChoices = ((1, "Agriculture"), (2, "Clothing Industry"), (3, "Computer Science/ IT"),
                         (4, "Construction"), (5, "Education"), (6, "Entertainment"), (7, "Finance/ Accounting"),
                         (8, "First Responder"),
                         (9, "Food Services"), (10, "Government Employee"), (11, "Law"), (12, "Medical Field"),
                         (13, "Military"), (14, "Other (In-person)"), (15, "Other (Virtual)"))
    occupation = forms.MultipleChoiceField(
        choices=occupationChoices,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    livingChoices = ((1, "Independent (1 person)"), (2, "Small Group (2-6)"),
                     (3, "Small Group Housing (7 - 20)"), (4, "Large Group Housing (21+)"),
                     (5, "Assisted Living"), (6, "Live with someone that is at risk"))
    living = forms.MultipleChoiceField(
        choices=livingChoices,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    # priority = forms.ChoiceField(
    #     choices=((1, 'low'), (2, 'medium'), (3, 'high')),
    #     required=True
    # )

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name',
        'address_line', 'zip_code', 'city', 'state', 'country']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
        patient = Patient(user=user)
        patient.age = self.cleaned_data.get('age')

        patient.occupation = self.cleaned_data.get('occupation')
        patient.preexisting = self.cleaned_data.get('preexisting')
        patient.living_situation = self.cleaned_data.get('living')
        # patient.priority = self.cleaned_data.get('priority')
        patient.save()

        return user


# class PatientApptBookForm(UserCreationForm):

    