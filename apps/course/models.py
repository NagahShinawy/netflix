from django.db import models


class ModelRepresentationMixin(models.Model):
    class Meta:
        abstract = True
        ordering = ["id"]


class Course(ModelRepresentationMixin, models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}-{self.title}"

    def students(self):
        return [student.to_pretty() for student in self.student.all()]


class Student(ModelRepresentationMixin, models.Model):
    fname = models.CharField(max_length=256, verbose_name="First Name")
    lname = models.CharField(max_length=256, verbose_name="Last Name")
    dob = models.DateField(null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name="student")

    def __str__(self):
        return f"{self.id}-{self.fname} {self.lname}".title()

    def to_pretty(self):
        return f"{self.fname}{self.lname}({self.pk})"

    def list_courses(self):
        return self.courses

    def grades(self):
        student_grades = CourseGrade.objects.filter(student__id=self.id)
        if student_grades:
            return [grade.to_pretty() for grade in student_grades]
        return "-"


class CourseGrade(models.Model):
    value = models.PositiveIntegerField(default=0)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="course_grades"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="grades")

    def __str__(self):
        return f"{self.id} - <{self.student} {self.course} {self.value}>"

    def to_pretty(self):
        return f"{self.course.title}({self.value})"


class Doctor(ModelRepresentationMixin, models.Model):
    fname = models.CharField(max_length=256)
    medical_centers = models.ManyToManyField(
        "course.MedicalCenter", null=True, blank=True, related_name="doctors"
    )

    def __str__(self):
        return f"{self.id}-{self.fname}"

    def medical_centers_list(self):
        medical_centers = self.medical_centers.all()
        if medical_centers:
            return [center.name for center in medical_centers]
        return "-"


class MedicalCenter(ModelRepresentationMixin, models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def doctors_list(self):
        doctors = self.doctors.all()
        if doctors:
            return [doctor.fname for doctor in doctors]
        return "-"

    def __str__(self):
        return f"{self.id}-{self.name}"


"""
>>> from apps.course.models import Student, Course
>>> john = Student.objects.first()
[DEBUG] [27/Aug/2021 09:19:10]
>>> john
<Student: 1-John James>
>>> john.courses
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 
0x00000205AA6F03C8>
>>> 
>>> john.courses.objects.all()
>>> Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'ManyRelatedManager' object has no attribute 'objects'

>>> john.courses.all()
<QuerySet [<Course: 1-django>, <Course: 2-flask>, <Course: 7-fastapi>, <Course: 8-drf>]>
>>> 
>>> leon = Student.objects.last()
>>> leon
<Student: 2-Loen Smith>
>>> leon.courses.all()
<QuerySet [<Course: 2-flask>, <Course: 3-react>, <Course: 4-js>, <Course: 5-pandas>, <Course: 6-numpy>, <Course: 8-drf>]>
>>> js = Course.objects.get(id=4)
>>> js
<Course: 4-js>
>>> js.student.all()
<QuerySet [<Student: 2-Loen Smith>, <Student: 3-Adam Gory>]>
"""
