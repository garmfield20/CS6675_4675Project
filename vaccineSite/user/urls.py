from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signup/distributor', views.distributor_sign_up, name='distributor_sign_up'),
    path('signup/physician', views.physician_sign_up, name='physician_sign_up'),
    path('signup/patient', views.patient_sign_up, name='patient_sign_up'),
    path('login', views.user_login, name='login'),  # finished

    # should contain: 'welcome {distributor name}' , rating score, days since last update
    # buttons to go to profile, view appointments, add appointments, and add vaccines 
    path('distributor', views.distributor_main, name='distributor_main'),
    path('distributor/profile', DistributorProfileView.as_view(), name='distributor_profile'),
    path('distributor/appointments', DistributorAppointmentView.as_view(), name='distributor_appointments'),
    path('distributor/appointments/add', views.distributor_appointments_add, name='distributor_appointments_add'),
    path('distributor/vaccine', views.vaccine, name='vaccine'),

    path('physician', PhysicianMain.as_view(), name='physician_main'),
    path('physician/profile', PhysicianProfileView.as_view(), name='physician_profile'),
    path('physician/appointments', PhysicianAvailableAppointments.as_view(), name='physician_appointments'),
    path('physician/appointments/<int:pk>', PhysicianAppointmentsBook.as_view(), name='physician_add_appointments'),
    path('physician/appointments/my', PhysicianMyAppointments.as_view(), name='physician_appointments_my'),

    path('patient', PatientMain.as_view(), name='patient_main'),
    path('patient/profile', PatientProfileView.as_view(), name='patient_profile'),
    path('patient/appointments', PatientAppointmentView.as_view(), name='patient_appointments'),
    path('patient/appointments/d', PatientAppointmentViewD.as_view(), name='patient_appointments_d'),
    path('patient/appointments/v', PatientAppointmentViewV.as_view(), name='patient_appointments_v'),
    path('patient/appointments/r', PatientAppointmentViewR.as_view(), name='patient_appointments_r'),
    path('patient/appointments/<int:pk>', PatientAppointmentsBook.as_view(), name='patient_appointments_book'),
    path('patient/appointments/my', PatientMyAppointments.as_view(), name='patient_appointments_my'),

    path('logout', views.log_out, name='logout')
]
