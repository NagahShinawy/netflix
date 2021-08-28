from django.db import models
from .choices import PositionChoices


class PM(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def developers_list(self):
        return [developer for developer in self.developers.all()]

    def projects_list(self):
        return [project for project in self.projects.all()]


class Project(models.Model):
    title = models.CharField(max_length=256)
    pm = models.ForeignKey(
        PM, on_delete=models.PROTECT, null=True, blank=True, related_name="projects"
    )
    developers = models.ManyToManyField(
        "series.Developer", null=True, blank=True, related_name="developers"
    )

    def developers_list(self):
        return [developer for developer in self.developers.all()]

    def __str__(self):
        return self.title


class Developer(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    position = models.CharField(
        max_length=2,
        choices=PositionChoices.choices,
        null=True,
        blank=True,
        default=PositionChoices.BACKEND,
    )
    team_lead = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.PROTECT
    )

    pm = models.ForeignKey(
        PM, on_delete=models.PROTECT, null=True, blank=True, related_name="developers"
    )
    is_tl = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.name
