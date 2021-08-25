from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated at")
    )  # last save

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(null=True, blank=True, verbose_name=_("Slug"))

    class Meta:
        abstract = True


class InfoMixin(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.TextField(
        max_length=225, null=True, blank=True, verbose_name=_("Description")
    )

    class Meta:
        abstract = True
