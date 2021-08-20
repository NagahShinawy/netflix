import logging
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from . import errors

# https://www.kite.com/blog/python/advanced-django-models-python-overview/

logger = logging.getLogger(__name__)


class Video(models.Model):
    class VideoStateOptions(models.TextChoices):
        PUBLISHED = "PU", "PUBLISH"  # db_value, user_display_value
        DRAFT = "DR", "DRAFT"
        UNLISTED = "UN", "Unlisted"
        PRIVATE = "PR", "Private"

    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.TextField(
        max_length=225, null=True, blank=True, verbose_name=_("Description")
    )
    slug = models.SlugField(null=True, blank=True, verbose_name=_("Slug"))
    video_id = models.CharField(
        max_length=225, default="id#", verbose_name=_("Media ID")
    )
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

    def __str__(self):
        id_ = self.id
        return f"{id_}-{self.slug}" if self.slug else f"{id_}-{self.title}"

    @property
    def is_published(self):
        return self.is_active

    def save(self, *args, **kwargs):
        video = f"{self.id}-{self.title}" if self.id else self.title
        if (
            self.state == self.VideoStateOptions.PUBLISHED
            and self.published_timestamp is None
        ):
            self.published_timestamp = timezone.now()

        elif self.state == self.VideoStateOptions.DRAFT:
            self.published_timestamp = None
        logger.info(
            f"Update 'published_timestamp' for video <{video}> to <{self.published_timestamp}>"
        )

        self.update_slug(video)

        return super(Video, self).save(*args, **kwargs)

    def update_slug(self, video):
        if not self.slug:
            logger.info(f"Update 'slug' for video <{video}> using title <{self.title}>")
            self.slug = slugify(self.title)
            logger.info(f"Updated 'slug' for video <{video}> to <{self.slug}>")

    def clean(self):
        if Video.objects.filter(title__iexact=self.title).exists():
            raise ValidationError(errors.DUPLICATED_TITLE)
        super(Video, self).clean()

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
