from django.contrib import admin

from .models import Student, Course, Doctor, MedicalCenter, CourseGrade

admin.site.register(CourseGrade)


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "students")
    # readonly_fields = ("id", "student__list_courses")  # todo: fix this
    readonly_fields = ("id", "students")
    search_fields = ("id", "title", "student__fname", "student__lname", "student__dob")


@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ("id", "fname", "lname", "grades")


@admin.register(Doctor)
class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ("id", "fname", "medical_centers_list")
    search_fields = ("fname", "medical_centers__name", "medical_centers__location")


@admin.register(MedicalCenter)
class MedicalCenterModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "doctors_list")
    search_fields = ("name", "doctors__fname")
