from django.db import models

# from django.utils.translation import gettext_lazy as _
from apps.core.db.models import (
    TimestampMixin,
    SlugMixin,
    InfoMixin,
    StateMixin,
    IsActiveMixin,
    PublishedTimestamp,
)
from .managers import PlaylistManager
from apps.core.utils.base import update_slug


class Playlist(
    TimestampMixin,
    SlugMixin,
    InfoMixin,
    StateMixin,
    IsActiveMixin,
    PublishedTimestamp,
    models.Model,
):

    objects = PlaylistManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        update_slug(instance=self)
        return super().save(*args, **kwargs)
