from django.urls import path, include
from RDV import views


urlpatterns = [
    path('Rdvs', views.RdvApi), 
    path('Doctors', views.DoctorApi), 
    path('Patients', views.PatientApi),
    path('Rdvs/<int:id>', views.RdvApi), 
    path('Doctors/<int:id>', views.DoctorApi),
    path('Patients/<int:id>', views.PatientApi)
]


