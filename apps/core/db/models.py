from django.db import models
from django.utils.translation import gettext_lazy as _
from .choices import StateOptions


class TimestampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"), null=True, blank=True)
    updated = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated at"), null=True, blank=True
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


class StateMixin(models.Model):
    state = models.CharField(
        max_length=2, choices=StateOptions.choices, default=StateOptions.DRAFT
    )

    class Meta:
        abstract = True


class IsActiveMixin(models.Model):
    is_active = models.BooleanField(default=False, verbose_name=_("Is Active"))

    class Meta:
        abstract = True


class PublishedTimestamp(models.Model):
    published_timestamp = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True, editable=False
    )

    class Meta:
        abstract = True
