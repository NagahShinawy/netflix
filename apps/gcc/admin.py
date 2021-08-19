from django.contrib import admin
from .models import MedicalCenter, Appointment


@admin.register(Appointment)
class AppointmentModelAdmin(admin.ModelAdmin):
    date_hierarchy = "dob"


admin.site.register(MedicalCenter)
