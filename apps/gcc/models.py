from django.db import models
from django.utils.translation import gettext_lazy as _


class MedicalCenter(models.Model):
    name = models.CharField(max_length=256, db_column="center_name")
    address = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=24)
    phone = models.CharField(max_length=24, blank=True)

    def __str__(self):
        if self.phone:
            return f"{self.name}-{self.phone}"
        return self.name


class Appointment(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = "new", _("New")
        IN_PROGRESS = "in_progress", _("In-Progress")
        RETURNED = "returned", _("Returned to Entry Clerk")
        SENT_FOR_APPROVAL = "sent_for_approval", _("Sent for Approval")
        FIT = "fit", _("Fit")
        UNFIT = "unfit", _("Unfit")
        REJECTED = "rejected", _("Rejected")
        REPORTED_AS_UNFIT = "reported_as_unfit", _("Reported as Unfit")
        EXPIRED = "expired", _("Expired")

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
    status = models.CharField(max_length=56, default=StatusChoices.NEW, choices=StatusChoices.choices)

    def __str__(self):
        fullname = f"{self.first_name} {self.last_name}"
        return fullname.title()
