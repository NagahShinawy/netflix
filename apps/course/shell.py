from .models import MedicalCenter, Doctor


def get_centers_for_doctor(doctor: Doctor):
    return doctor.medical_centers.all()


def get_doctors_of_center(center: MedicalCenter):
    return center.doctors.all()


def get_doctors_names():
    return Doctor.objects.all().values("id", "fname")


def get_centers_names():
    return MedicalCenter.objects.all().values("id", "name")