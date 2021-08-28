import datetime
import logging
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .managers import VideoManager
from .validators import MinYearValidator, MaxYearValidator
from .errors import DuplicatedVideoTitle
from .choices import VideoStateOptions
from apps.core.db.models import (
    TimestampMixin,
    SlugMixin,
    InfoMixin,
    StateMixin,
    IsActiveMixin,
    PublishedTimestamp,
)
from apps.playlist.models import Playlist

# https://www.kite.com/blog/python/advanced-django-models-python-overview/ (proxy models)
# https://georgexyz.com/django-model-form-validation.html  (validations)
from apps.core.managers import PublishedVideoManager

logger = logging.getLogger(__name__)


class Video(
    TimestampMixin,
    InfoMixin,
    SlugMixin,
    StateMixin,
    IsActiveMixin,
    PublishedTimestamp,
    models.Model,
):
    class Year:
        MIN = 1930
        max_ = datetime.datetime.now().year

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=225, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    video_id = models.CharField(max_length=225)
    is_published = models.BooleanField(default=False)
    objects = models.manager
    video_id = models.CharField(max_length=225, verbose_name=_("Media ID"), unique=True)

    year = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinYearValidator(Year.MIN), MaxYearValidator(Year.max_)],
    )
    playlist = models.ForeignKey(
        Playlist,
        on_delete=models.SET_NULL,
        related_name="videos",
        verbose_name=_("Playlist"),
        blank=True,
        null=True,
    )  # frst = Playlist.objects.first()  ==> frst.video.all()  # 'video' is related_name
    objects = VideoManager()

    def __str__(self):
        id_ = self.id
        return f"{id_}-{self.slug}" if self.slug else f"{id_}-{self.title}"

    @property
    def is_published(self):
        return self.is_active and self.state == VideoStateOptions.PUBLISHED

    @property
    def is_draft(self):
        return self.state == VideoStateOptions.DRAFT

    @property
    def is_unlisted(self):
        return self.state == VideoStateOptions.UNLISTED

    @property
    def is_private(self):
        return self.state == VideoStateOptions.PRIVATE

    def clean(self):
        if (
            Video.objects.is_exists(field="title", value=self.title)
            and self.slug is None
        ):
            raise ValidationError(DuplicatedVideoTitle.message)

        super(Video, self).clean()

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

    objects = PublishedVideoManager()

    class Meta:
        proxy = True
        verbose_name = "Published Video"
        verbose_name_plural = "Published Videos"
        ordering = ["id"]
        verbose_name = "Video"  # add
        verbose_name_plural = "Table Videos"  #
