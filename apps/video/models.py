from django.db import models
from apps.core.managers import HondaManager, BMWManager


# https://www.kite.com/blog/python/advanced-django-models-python-overview/


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=225, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    video_id = models.CharField(max_length=225)
    objects = models.manager

    def __str__(self):
        id_ = self.id
        return f"{id_}-{self.slug}" if self.slug else f"{id_}-{self.title}"

    class Meta:
        ordering = ["-id"]
        verbose_name = "Movie Video"  # add
        verbose_name_plural = "Netflix Videos"  #


class VideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy


# multi-table inheritance example
class Vehicle(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=80)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.pk}-{self.model}"

    class Meta:  # more/extra options
        ordering = ["-id"]


class Airplane(Vehicle):
    is_cargo = models.BooleanField(default=False)
    is_passenger = models.BooleanField(default=True)


class MotorBike(Vehicle):
    fuel = models.CharField(max_length=50)


# proxy model example
class Car(models.Model):
    vin = models.CharField(max_length=17)
    model = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=80)
    year = models.IntegerField()

    def __str__(self):
        return f"Car is --> {self.model}"


class Honda(Car):
    objects = HondaManager()

    def __str__(self):
        return f"<{self.model}>"

    class Meta:
        proxy = True


class BMW(Car):
    objects = BMWManager()

    def __str__(self):
        return f"[{self.model}]"

    class Meta:
        proxy = True
