from django.test import TestCase
from .models import MedicalCenter, Doctor


class DoctorCenterTestCaseMixin(TestCase):
    def setUp(self) -> None:
        self.mayo = MedicalCenter.objects.create(name="Mayo Clinic")
        self.toronto = MedicalCenter.objects.create(name="Toronto Clinic")
        self.medical_centers = [self.mayo, self.toronto]
        self.john = Doctor.objects.create(fname="John")
        self.john.medical_centers.set(self.medical_centers)
        self.john.save()


class DoctorModelTestCase(DoctorCenterTestCaseMixin):

    def test_add_doctor(self):
        self.assertEqual(Doctor.objects.all().count(), 1)

    def test_doctor_name(self):
        self.assertEqual(self.john.fname, "John")

    def test_related_centers(self):
        john_centers = self.john.medical_centers.all()
        self.assertEqual(john_centers.count(), len(self.medical_centers))
        self.assertEqual(john_centers.first(), self.mayo)
        self.assertEqual(john_centers.first().name, self.mayo.name)


class MedicalCenterTestCase(DoctorCenterTestCaseMixin):

    def test_create_medical_centers(self):
        self.assertEqual(MedicalCenter.objects.all().count(), len(self.medical_centers))

    def test_doctors_joined_to_medical_centers(self):
        doctors = Doctor.objects.all()
        mayo_doctors = self.mayo.doctors.all()
        toronto_doctors = self.toronto.doctors.all()
        self.assertEqual(mayo_doctors.count(), doctors.count())
        self.assertEqual(toronto_doctors.count(), doctors.count())








