from django.db import models


# https://www.kite.com/blog/python/advanced-django-models-python-overview/


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=225, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    video_id = models.CharField(max_length=225, default="id#")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        id_ = self.id
        return f"{id_}-{self.slug}" if self.slug else f"{id_}-{self.title}"

    @property
    def is_published(self):
        return self.is_active

    class Meta:
        ordering = ["id"]
        verbose_name = "Video"  # add
        verbose_name_plural = "Table Videos Show"  #


class PublishedVideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy
        verbose_name = "Video"
        verbose_name_plural = "Published Videos Show"


class NotPublishedVideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy
        verbose_name = "Video"
        verbose_name_plural = "Not Published Videos Show"
