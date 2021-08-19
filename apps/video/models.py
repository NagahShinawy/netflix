from django.db import models
from django.utils.translation import gettext_lazy as _


# https://www.kite.com/blog/python/advanced-django-models-python-overview/


class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.TextField(max_length=225, null=True, blank=True, verbose_name=_("Description"))
    slug = models.SlugField(null=True, blank=True, verbose_name=_("Slug"))
    video_id = models.CharField(max_length=225, default="id#", verbose_name=_("Media ID"))
    is_active = models.BooleanField(default=False, verbose_name=_("Is Active"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    def __str__(self):
        id_ = self.id
        return f"{id_}-{self.slug}" if self.slug else f"{id_}-{self.title}"

    @property
    def is_published(self):
        return self.is_active

    class Meta:
        ordering = ["id"]
        verbose_name = "Video"  # add
        verbose_name_plural = "Table Videos"  #


class PublishedVideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy
        verbose_name = "Video"
        verbose_name_plural = "Published Videos"


class NotPublishedVideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy
        verbose_name = "Video"
        verbose_name_plural = "Not Published Videos"
