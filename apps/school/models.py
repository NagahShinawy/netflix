from django.db import models

# https://dev.to/sankalpjonna/using-abstract-models-in-django-1igi

# ########### # ############ Abstract Models ############ ############ ############ ############ ############


class Person(models.Model):
    name = models.CharField(max_length=256)
    dob = models.DateTimeField(verbose_name="Date of Birth")
    joined_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.dob}"

    class Meta:
        abstract = True


class SchoolEmployee(Person):
    compensation = models.CharField(max_length=256)

    class Meta:
        abstract = True


class HiredHelp(SchoolEmployee):
    shift_timings = models.JSONField()

    class Meta:
        abstract = True


# ########### # ############ Actual Models ############ ############ ############ ############ ############


class Student(Person):
    roll_num = models.IntegerField()


class Teacher(SchoolEmployee):
    qualifications = models.JSONField()


class CleaningMember(HiredHelp):
    pass





