from django.urls import path

from .views import Doctor_ListView, DoctorDetailView, DoctorAvailabilityView, DoctorAppointmentView

urlpatterns = [
    path('doctor_list/', Doctor_ListView.as_view(), name='doctor-list'),
    path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctor_availability/<int:pk>/', DoctorAvailabilityView.as_view(), name='doctor-availability'),
    path('doctor_appointment/<int:pk>/', DoctorAppointmentView.as_view(), name='doctor-appointment'),
]
