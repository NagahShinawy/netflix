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

    def get_videos_ids(self):
        return self.videos.all().values_list("id", "title", "playlist_id")

    def related_videos(self):
        videos = self.videos.all().values_list("title")
        return ". ".join([f"{counter}-{video[0]}" for counter, video in enumerate(videos, start=1)])
