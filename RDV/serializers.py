from rest_framework import serializers
from RDV.models import Rdv, Doctor, Patient


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        
    
class RdvSerializer(serializers.ModelSerializer):
    doctorId = DoctorSerializer(read_only=True)
    patientId = PatientSerializer(read_only=True)
    class Meta:
        model = Rdv
        fields = "__all__"
