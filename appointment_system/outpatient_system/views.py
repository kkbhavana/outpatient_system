from django.shortcuts import render
from rest_framework import generics

from .models import Doctor_List, Appointment_List
from .serializers import DoctorListSerializer, Appointment_ListSerializer


# Create your views here.
class Doctor_ListView(generics.ListAPIView):
    queryset = Doctor_List.objects.all()
    serializer_class = DoctorListSerializer


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor_List.objects.all()
    serializer_class = DoctorListSerializer


class DoctorAvailabilityView(generics.ListAPIView):
    serializer_class = DoctorListSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        return Doctor_List.objects.filter(id=id)


class DoctorAppointmentView(generics.CreateAPIView):
    queryset = Appointment_List.objects.all()
    serializer_class = Appointment_ListSerializer
