from rest_framework import serializers

from .models import Doctor_List, Appointment_List


class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_List
        fields = ['name', 'specialization', 'appointment_date', 'available_time']


class Appointment_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment_List
        fields = ['doctor_name', 'appointment_time']
