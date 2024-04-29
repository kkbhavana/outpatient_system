from django.contrib import admin

from .models import Doctor_List, Appointment_List

# Register your models here.
admin.site.register(Doctor_List)
admin.site.register(Appointment_List)
