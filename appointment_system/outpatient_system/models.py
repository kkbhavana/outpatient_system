from django.db import models


# Create your models here.
class Doctor_List(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    appointment_date = models.CharField(max_length=100)
    available_time = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment_List(models.Model):
    doctor_name = models.ForeignKey(Doctor_List, on_delete=models.CASCADE)
    appointment_time = models.CharField(max_length=100)

    def __str__(self):
        return str(self.doctor_name)
