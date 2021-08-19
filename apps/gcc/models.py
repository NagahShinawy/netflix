from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


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
    medical_center = models.ForeignKey(
        "MedicalCenter", on_delete=models.PROTECT, null=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    status = models.CharField(
        max_length=56, default=StatusChoices.NEW, choices=StatusChoices.choices
    )

    def __str__(self):
        fullname = f"{self.first_name} {self.last_name}"
        print(self.age)
        return fullname.title()

    @property
    def is_expired(self):
        return self.status == self.StatusChoices.EXPIRED

    @property
    def is_new(self):
        return self.status == self.StatusChoices.NEW

    @property
    def is_fit(self):
        return self.status == self.StatusChoices.FIT

    @property
    def is_unfit(self):
        return self.status == self.StatusChoices.UNFIT

    @property
    def can_be_printed(self):
        return any(
            [
                self.StatusChoices.FIT,
                self.StatusChoices.UNFIT,
                self.StatusChoices.REJECTED,
                self.StatusChoices.REPORTED_AS_UNFIT,
                self.StatusChoices.EXPIRED,
            ]
        )

    @property
    def age(self):
        if not self.dob:
            return
        now = timezone.now()
        return now.year - self.dob.year - ((now.month, now.day) < (self.dob.month, self.dob.day))


class AppointmentStatusHistory(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="status_history")
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=56, choices=Appointment.StatusChoices.choices)
    # raw username here to save history in case of user instance deletion
    username = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.status}: {self.timestamp}"