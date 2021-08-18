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
        verbose_name_plural = "Netflix Videos"  #


class VideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy
