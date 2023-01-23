from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RDV.models import Rdv, Doctor, Patient
from RDV.serializers import RdvSerializer, DoctorSerializer, PatientSerializer

LEGAL_DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
# Create your views here.

@csrf_exempt
def RdvApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            rdvs = Rdv.objects.all()
            rdvs_serializer = RdvSerializer(rdvs, many=True)
            return JsonResponse(rdvs_serializer.data, safe=False)
        else:
            rdv = Rdv.objects.get(RdvId=id)
            rdv_serializer = RdvSerializer(rdv)
            return JsonResponse(rdv_serializer.data, safe=False)
    elif request.method == 'POST':
        rdv_data = JSONParser().parse(request)
        rdv_serializer = RdvSerializer(data=rdv_data)
        if rdv_serializer.is_valid():
            rdv_serializer.save()
            return JsonResponse(rdv_serializer.data, safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        rdv_data = JSONParser().parse(request)
        rdv = Rdv.objects.get(RdvId=rdv_data['RdvId'])
        rdv_serializer = RdvSerializer(rdv, data=rdv_data)
        if rdv_serializer.is_valid():
            rdv_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == 'DELETE':
        rdv = Rdv.objects.get(RdvId=id)
        rdv.delete()
        return JsonResponse("Deleted successfully", safe=False)

@csrf_exempt
def DoctorApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            doctors = Doctor.objects.all()
            doctors_serializer = DoctorSerializer(doctors, many=True)
            return JsonResponse(doctors_serializer.data, safe=False)
        else:
            doctor = Doctor.objects.get(DoctorId=id)
            doctor_serializer = DoctorSerializer(doctor)
            return JsonResponse(doctor_serializer.data, safe=False)
    elif request.method == 'POST':
        doctor_data = JSONParser().parse(request)
        doctor_serializer = DoctorSerializer(data=doctor_data)
        contraints = True
        if len(str(doctor_data['StartTime']).split(":")) != 2 or len(str(doctor_data['EndTime']).split(":")) != 2:
            contraints = False
        days = str(doctor_data['WorkDays']).split(',')
        for day in days:
            if day not in LEGAL_DAYS:
                contraints = False
                break
        if doctor_serializer.is_valid() and contraints:
            doctor_serializer.save()
            return JsonResponse(doctor_serializer.data, safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        doctor_data = JSONParser().parse(request)
        doctor = Doctor.objects.get(DoctorId=doctor_data['DoctorId'])
        doctor_serializer = DoctorSerializer(doctor, data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == 'DELETE':
        doctor = Doctor.objects.get(DoctorId=id)
        doctor.delete()
        return JsonResponse("Deleted successfully", safe=False)

@csrf_exempt
def PatientApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            patients = Patient.objects.all()
            patients_serializer = PatientSerializer(patients, many=True)
            return JsonResponse(patients_serializer.data, safe=False)
        else:
            patient = Patient.objects.get(PatientId=id)
            patient_serializer = PatientSerializer(patient)
            return JsonResponse(patient_serializer.data, safe=False)
    elif request.method == 'POST':
        patient_data = JSONParser().parse(request)
        patient_serializer = PatientSerializer(data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse(patient_serializer.data, safe=False)
        return JsonResponse("Failed to add")
    elif request.method == 'PUT':
        patient_data = JSONParser().parse(request)
        patient = Patient.objects.get(PatientId=patient_data['DoctroId'])
        patient_serializer = PatientSerializer(patient, data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == 'DELETE':
        patient = Patient.objects.get(PatientId=id)
        patient.delete()
        return JsonResponse("Deleted successfully", safe=False)
