from django.db import models


class MedicalReport(models.Model):
    title = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
