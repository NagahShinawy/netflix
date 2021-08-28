from django.db import models


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
    pass


class Season(TVShowModelMixin):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="seasons")


class Episode(TVShowModelMixin):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="episodes", null=True, blank=True)
