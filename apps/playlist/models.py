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
        return ", ".join([str(video[0]) for video in self.videos.all().values_list("id")])

    def related_videos(self):
        videos = self.videos.all().values_list("title")
        videos_titles = [video[0] for video in videos]
        if videos_titles:
            return ". ".join([f"{counter}-{video}" for counter, video in enumerate(videos_titles, start=1)])
        return "-"

    def total_videos(self):
        return self.videos.all().count()
