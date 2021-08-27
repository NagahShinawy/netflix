from django.test import TestCase
from .models import MedicalCenter, Doctor


class DoctorModelTestCase(TestCase):

    def setUp(self) -> None:
        self.mayo = MedicalCenter.objects.create(name="Mayo Clinic")
        self.toronto = MedicalCenter.objects.create(name="Toronto Clinic")
        self.medical_centers = [self.mayo, self.toronto]
        self.john = Doctor.objects.create(fname="John")
        self.john.medical_centers.set(self.medical_centers)
        self.john.save()

    def test_add_doctor(self):
        self.assertEqual(Doctor.objects.all().count(), 1)

    def test_doctor_name(self):
        self.assertEqual(self.john.fname, "John")

    def test_related_centers(self):
        john_centers = self.john.medical_centers.all()
        self.assertEqual(john_centers.count(), len(self.medical_centers))
        self.assertEqual(john_centers.first(), self.mayo)
        self.assertEqual(john_centers.first().name, self.mayo.name)





