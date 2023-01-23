from django.db import models

# Create your models here.

class Doctor(models.Model):
    DoctorId = models.AutoField(primary_key=True)
    DoctorFirstName = models.CharField(max_length=500)
    DoctorLastName = models.CharField(max_length=500)
    DoctorSpeciality = models.CharField(max_length=500)
    DoctorEmail = models.CharField(max_length=500)
    DoctorAddress = models.CharField(max_length=500)
    StartTime = models.CharField(max_length=8, default="09:00")
    EndTime = models.CharField(max_length=8, default="17:00")
    Interval = models.IntegerField(default=30)
    WorkDays = models.CharField(max_length=500, default="Sun,Mon,Tue,Wed,Thu")
    DoctorPassword = models.CharField(max_length=500, default="doctor1")
    Latitude = models.FloatField(default=36.711823)
    Longitude = models.FloatField(default=4.051717)


class Patient(models.Model):
    PatientId = models.AutoField(primary_key=True)
    PatientFirstName = models.CharField(max_length=500)
    PatientLastName = models.CharField(max_length=500)
    PatientEmail = models.CharField(max_length=500)
    PatientAddress = models.CharField(max_length=500)


class Rdv(models.Model):
    RdvId = models.AutoField(primary_key=True)
    RdvDoctor = models.ForeignKey(Doctor,null=True, related_name='doctorId', on_delete=models.CASCADE)
    RdvPatient = models.ForeignKey(Patient, null=True, related_name='patientId', on_delete=models.CASCADE)
    Date = models.DateTimeField()
