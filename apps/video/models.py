from django.db import models


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
        verbose_name_plural = "Table Show Videos"  #


class VideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy [check proxy-model branch]
        verbose_name = "Movie Video"  # add
        verbose_name_plural = "Basic Video Title Show"  # left side show

    def __str__(self):
        return f"[{self.title}]"


class FastEditVideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy [check proxy-model branch]
        ordering = ["title"]
        verbose_name = "Editable Video"  # add btn
        verbose_name_plural = "Fast Edit Videos"  # left side view


class PublishedVideoProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Publish Video"
        verbose_name_plural = "Published Videos"


class H(models.Model):
    name = models.CharField(max_length=10)