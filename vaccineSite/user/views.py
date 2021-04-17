from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from django.http import HttpResponse
from django.template import loader

from .forms import PhysicianSignUpForm, DistributorSignUpForm, PatientSignUpForm, VaccineForm, CreateUserForm, \
    DistributorApptAddForm, PhysicianApptAddForm
from .models import Account, Distributor, Appointment, Patient, Vaccine, Physician
from .decorators import patient_required, physician_required, distributor_required


def signup(request):
    return render(request, 'user/signup.html')


def user_login(request):
    form = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_distributor:
                return redirect('distributor_main')
            elif user.is_physician:
                return redirect('physician_main')
            elif user.is_patient:
                return redirect('patient_main')
            else:
                messages.info(request, 'Not recognized account type')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'user/login.html', context={'form': form})


def log_out(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return render(request, 'user/logout.html')


@login_required
@distributor_required
def distributor_main(request):
    return render(request, 'user/distributor.html')


@method_decorator([login_required, distributor_required], name='dispatch')
class DistributorProfileView(ListView):
    model = Distributor
    template_name = 'user/distributor_profile.html'

    def get_queryset(self):
        distributor_query = Distributor.objects.get(user=self.request.user)
        physician_query = Physician.objects.get(distributor=distributor_query)
        return distributor_query


@method_decorator([login_required, distributor_required], name='dispatch')
class AppointmentView(ListView):
    model = Appointment
    template_name = 'user/distributor_appointments.html'

    def get_queryset(self):
        queryset = Appointment.objects.all()
        filtered_queryset = [_ for _ in queryset if _.distributor.user.username == self.request.user.username]
        return filtered_queryset


@login_required
@distributor_required
def distributor_appointments_add(request):
    form = DistributorApptAddForm()
    if request.method == 'POST':
        form = DistributorApptAddForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('distributor_appointments')

    context = {'form': form}
    return render(request, 'user/distributor_appointments_add.html', context)


@login_required
@distributor_required
def vaccine(request):
    form = VaccineForm()
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('distributor_main')
    context = {'form': form}
    return render(request, 'user/distributor_vaccine.html', context)


@login_required
@patient_required
def patient_main(request):
    return render(request, 'user/patient.html')


@method_decorator([login_required, patient_required], name='dispatch')
class PatientProfileView(ListView):
    model = Patient
    template_name = 'user/patient_profile.html'

    def get_queryset(self):
        queryset = Patient.objects.all()
        filtered_queryset = [_ for _ in queryset if _.user.username == self.request.user.username]
        return filtered_queryset


@method_decorator([login_required, patient_required], name='dispatch')
class PatientAppointmentView(ListView):
    model = Appointment
    template_name = 'user/patient_appointments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@login_required
@patient_required
def patient_appointments_book(request):
    return render(request, 'user/patient_appointments_book.html')


@login_required
@physician_required
def physician_main(request):
    return render(request, 'user/physician.html')


@method_decorator([login_required, physician_required], name='dispatch')
class PhysicianProfileView(ListView):
    model = Physician
    template_name = 'user/physician_profile.html'

    def get_queryset(self):
        queryset = Physician.objects.all()
        filtered_queryset = [_ for _ in queryset if _.user.username == self.request.user.username]
        return filtered_queryset


@login_required
@physician_required
def physician_appointments(request):
    form = PhysicianApptAddForm()
    if request.method == 'POST':
        form = PhysicianApptAddForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('physician_profile')

    context = {'form': form}
    return render(request, 'user/physician_appointments_add.html', context)


def distributor_sign_up(request):
    form = DistributorSignUpForm()
    if request.method == 'POST':
        form = DistributorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'user/distributor_signup.html', context)


def patient_sign_up(request):
    form = PatientSignUpForm()
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'user/patient_signup.html', context)


def physician_sign_up(request):
    form = PhysicianSignUpForm()
    if request.method == 'POST':
        form = PhysicianSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'user/physician_signup.html', context)
