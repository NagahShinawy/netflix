from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.db.models import TimestampMixin, SlugMixin, InfoMixin
from apps.video.models import Video


class Playlist(TimestampMixin, SlugMixin, InfoMixin, models.Model):
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name="playlist",
        verbose_name=_("Video"),
    )
