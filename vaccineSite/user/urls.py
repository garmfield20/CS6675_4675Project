from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signup/distributor', views.distributor_sign_up, name='distributor_sign_up'),
    path('signup/physician', views.physician_sign_up, name='physician_sign_up'),
    path('signup/patient', views.patient_sign_up, name='patient_sign_up'),
    path('login', views.user_login, name='login'),
    path('login/distributor', views.distributor_log_in, name='distributor_log_in'),
    path('login/physician', views.physician_log_in, name='physician_log_in'),
    path('login/patient', views.patient_log_in, name='patient_log_in'),
    path('logout', views.log_out, name='logout')
]