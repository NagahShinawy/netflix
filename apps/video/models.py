import datetime
import logging
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from .managers import VideoManager
from .validators import MinYearValidator, MaxYearValidator
from .errors import DuplicatedVideoTitle
from .choices import VideoStateOptions

# https://www.kite.com/blog/python/advanced-django-models-python-overview/ (proxy models)
# https://georgexyz.com/django-model-form-validation.html  (validations)

logger = logging.getLogger(__name__)


class Video(models.Model):
    class Year:
        MIN = 1930
        max_ = datetime.datetime.now().year

    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.TextField(
        max_length=225, null=True, blank=True, verbose_name=_("Description")
    )
    slug = models.SlugField(null=True, blank=True, verbose_name=_("Slug"))
    video_id = models.CharField(max_length=225, verbose_name=_("Media ID"), unique=True)
    is_active = models.BooleanField(default=False, verbose_name=_("Is Active"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated at")
    )  # last save
    state = models.CharField(
        max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT
    )
    published_timestamp = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True, editable=False
    )

    year = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinYearValidator(Year.MIN), MaxYearValidator(Year.max_)],
    )
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

    def save(self, *args, **kwargs):
        video = f"{self.id}-{self.title}" if self.id else self.title
        is_published = self.state == VideoStateOptions.PUBLISHED
        if is_published and self.published_timestamp is None:
            self.published_timestamp = timezone.now()

        if is_published and self.published_timestamp:
            self.is_active = True

        elif self.is_draft:
            self.published_timestamp = None
        logger.info(
            f"Update 'published_timestamp' for video <{video}> to <{self.published_timestamp}>"
        )

        return super(Video, self).save(*args, **kwargs)

    def clean(self):
        if (
            Video.objects.filter(title__iexact=self.title).exists()
            and self.slug is None
        ):
            raise ValidationError(DuplicatedVideoTitle.message)
        else:
            self.slug = slugify(self.title)

        super(Video, self).clean()

    class Meta:
        ordering = ["id"]
        verbose_name = "Video"  # add
        verbose_name_plural = "Table Videos"  #
