from .models import MedicalCenter, Doctor


def get_centers_for_doctor(doctor: Doctor):
    return doctor.medical_centers.all()


def get_doctors_of_center(center: MedicalCenter):
    return center.doctors.all()


def get_doctors_names():
    return Doctor.objects.all().values("id", "fname")


def get_centers_names():
    return MedicalCenter.objects.all().values("id", "name")

"""
>>> from apps.course.shell import *
>>> mina = Docotor.objects.get(id=5)
>>> Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Docotor' is not defined

>>> mina = Doctor.objects.get(id=5)
[DEBUG] [27/Aug/2021 10:02:24] in [C:\Users\Nagaj\AppData\Local\Programs\Python\Python37\lib\asyncio\selector_events.py/__init__:#58] [Using selector: SelectSelector]
>>> mina
<Doctor: 5-mina>
>>> get_centers_for_doctor(mina)
<QuerySet [<MedicalCenter: 1-police hospital>, <MedicalCenter: 3-mersal>]>
>>> get_centers_for_doctor(Doctor.objects.get(id=1))
<QuerySet [<MedicalCenter: 2-57357>, <MedicalCenter: 3-mersal>]>
>>> 
>>> mersal = MedicalCenter.objects.get(id=3)
>>> mersal
<MedicalCenter: 3-mersal>
>>> get_doctors_of_center(mersal)
<QuerySet [<Doctor: 1-mohammed>, <Doctor: 2-ahmed>, <Doctor: 3-mahmoud>, <Doctor: 4-karim>, <Doctor: 5-mina>]>
>>> mersal = MedicalCenter.objects.get(id=1)
>>> mersal
<MedicalCenter: 1-police hospital>
>>> plc = mersal
>>> plc
<MedicalCenter: 1-police hospital>
>>> get_doctors_of_center(mina)
>>> Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "E:\containers\learn-projects\netflix\apps\course\shell.py", line 9, in get_doctors_of_center
    return center.doctors.all()
AttributeError: 'Doctor' object has no attribute 'doctors'


>>> >>> get_doctors_of_center(plc)
<QuerySet [<Doctor: 5-mina>]>
>>> get_doctors_of_center(MedicalCenter.objects.get(id=2))
<QuerySet [<Doctor: 1-mohammed>]>
>>> 
"""