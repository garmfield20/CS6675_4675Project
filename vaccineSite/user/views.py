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

from .forms import PhysicianSignUpForm, DistributorSignUpForm, PatientSignUpForm, CreateUserForm
from .models import Account, Distributor, Appointment
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

@login_required
@distributor_required
def distributor_profile(request):
    return render(request, 'user/distributor_profile.html')


@method_decorator([login_required, distributor_required], name='dispatch')
class AppointmentView(ListView):
    model = Appointment
    template_name = 'user/distributor_appointments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@login_required
@distributor_required
def distributor_appointments_add(request):
    return render(request, 'user/distributor_appointments_add.html')


@login_required
@patient_required
def patient_main(request):
    return render(request, 'user/patient.html')

@login_required
@patient_required
def patient_profile(request):
    return render(request, 'user/patient_profile.html')

@login_required
@patient_required
def patient_appointments(request):
    return render(request, 'user/patient_appointments.html')

@login_required
@patient_required
def patient_appointments_book(request):
    return render(request, 'user/patient_appointments_book.html')


@login_required
@physician_required
def physician_main(request):
    return render(request, 'user/physician.html')
    

@login_required
@physician_required
def physician_profile(request):
    return render(request, 'user/physician_profile.html')




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


