from django.contrib import admin

from .models import Student, Course, Doctor, MedicalCenter

admin.site.register(Student)
admin.site.register(Course)


@admin.register(Doctor)
class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ("id", "fname", "medical_centers_list")


@admin.register(MedicalCenter)
class MedicalCenterModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "doctors_list")