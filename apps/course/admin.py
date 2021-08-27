from django.contrib import admin

from .models import Student, Course, Doctor, MedicalCenter

admin.site.register(Student)
admin.site.register(Course)


@admin.register(Doctor)
class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ("id", "fname", "medical_centers_list")
    search_fields = ("fname", "medical_centers__name", "medical_centers__location")


@admin.register(MedicalCenter)
class MedicalCenterModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "doctors_list")
    search_fields = ("name", "doctors__fname")
