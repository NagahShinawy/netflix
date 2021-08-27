from django.test import TestCase
from .models import MedicalCenter, Doctor


class DoctorCenterTestCaseMixin(TestCase):
    def setUp(self) -> None:
        self.mayo = MedicalCenter.objects.create(name="Mayo Clinic")
        self.toronto = MedicalCenter.objects.create(name="Toronto Clinic")
        self.mersal = MedicalCenter.objects.create(name="Mersal Clinic")
        self.medical_centers = [self.mayo, self.toronto, self.mersal]
        self.john = Doctor.objects.create(fname="John")
        self.adam = Doctor.objects.create(fname="Adam")
        self.mersal.doctors.add(self.adam)
        # self.john.medical_centers.set(self.medical_centers)
        self.john.medical_centers.set(MedicalCenter.objects.all())
        self.john.save()
        self.doctors = [self.adam, self.john]


class DoctorModelTestCase(DoctorCenterTestCaseMixin):
    def test_add_doctor(self):
        self.assertEqual(Doctor.objects.all().count(), len(self.doctors))

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
        self.assertEqual(mayo_doctors.count(), 1)
        self.assertEqual(toronto_doctors.count(), 1)

    def test_remove_medical_center_of_doctor(self):
        self.mayo.doctors.remove(self.john)
        self.assertEqual(self.mayo.doctors.all().count(), 0)  # now mayo has no doctors
        self.assertEquals(
            self.john.medical_centers.all().count(), len(self.medical_centers) - 1
        )  # now mayo removed from john related centers list
