from django.db import models


class MedicalCenter(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=24)
    phone = models.CharField(max_length=24, blank=True)

    def __str__(self):
        if self.phone:
            return f"{self.name}-{self.phone}"
        return self.name


class Appointment(models.Model):
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=256)
    # Deleting the medical center 'german su' would require deleting the following protected related objects:
    # You can not delete medical center unless you delete protected related objs first
    # suppose we have 3 appointments at medical center 'german hospital', so you can not delete 'german hospital'
    # unless you delete all objs [ 3 appointments ] related to that hospital 'german hospital (FK)'
    medical_center = models.ForeignKey("MedicalCenter", on_delete=models.PROTECT, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()

    def __str__(self):
        fullname = f"{self.first_name} {self.last_name}"
        return fullname.title()
