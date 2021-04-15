from django.urls import path
from . import views
from .views import AppointmentView, PatientAppointmentView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signup/distributor', views.distributor_sign_up, name='distributor_sign_up'),
    path('signup/physician', views.physician_sign_up, name='physician_sign_up'),
    path('signup/patient', views.patient_sign_up, name='patient_sign_up'),
    path('login', views.user_login, name='login'),

    # should contain: 'welcome {distributor name}' , rating score, days since last update
    # buttons to go to profile, view appointments, add appointments, and add vaccines 
    path('distributor', views.distributor_main, name='distributor_main'),
    path('distributor/profile', views.distributor_profile, name = 'distributor_profile'),
    path('distributor/appointments', AppointmentView.as_view(), name='distributor_appointments'),
    path('distributor/appointments/add', views.distributor_appointments_add, name = 'distributor_appointments_add'),
    path('distributor/vaccine', views.vaccine, name = 'vaccine'),

    path('physician', views.physician_main, name='physician_main'),
    path('physician/profile', views.physician_profile, name = 'physician_profile'),
    path('physician/appointments', views.physician_appointments, name = 'physician_appointments'),

    path('patient', views.patient_main, name='patient_main'),
    path('patient/profile', views.patient_profile, name = 'patient_profile'),
    path('patient/appointments', PatientAppointmentView.as_view(), name = 'patient_appointments'),
    path('patient/appointments/book', views.patient_appointments_book, name = 'patient_appointments_book'),

    

    path('logout', views.log_out, name='logout')
]