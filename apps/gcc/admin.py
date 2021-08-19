from django.contrib import admin
from .models import MedicalCenter, Appointment, AppointmentStatusHistory


@admin.register(Appointment)
class AppointmentModelAdmin(admin.ModelAdmin):
    date_hierarchy = "dob"


admin.site.register(MedicalCenter)
admin.site.register(AppointmentStatusHistory)
