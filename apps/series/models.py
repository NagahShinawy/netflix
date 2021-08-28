from django.db import models
from .choices import CategoryChoices, PositionChoices


class TVShowModelMixin(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["id"]

    def __str__(self):
        return self.title


class Series(TVShowModelMixin):
    category = models.CharField(
        max_length=2, choices=CategoryChoices.choices, default=CategoryChoices.COMEDY
    )

    def seasons_list(self):
        return [season.title for season in self.seasons.all()]


class Season(TVShowModelMixin):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="seasons")


class Episode(TVShowModelMixin):
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name="episodes", null=True, blank=True
    )


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

    def __str__(self):
        return self.name
