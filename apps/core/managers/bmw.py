from django.db import models


class BMWManager(models.Manager):
    BMW = "BMW"

    def get_queryset(self):
        return super().get_queryset().filter(model__icontains=self.BMW)