import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from .models import Video
from .choices import VideoStateOptions
from .proxy import (
    PublishedVideoProxy,
    NotPublishedVideoProxy,
    PrivateVideoProxy,
    FastEditVideoProxy,
    UnlistedVideoProxy,
    DraftVideoProxy,
    VideoProxy,
)

logger = logging.getLogger(__name__)


def get_video_representation(instance):
    video = f"{instance.id}-{instance.title}" if instance.id else instance.title
    return video


def update_slug(instance):
    video = get_video_representation(instance)
    if instance.slug is None:
        instance.slug = slugify(instance.title)
        logger.info(f"Update 'slug' for video <{video}> to <{instance.slug}>")


@receiver(pre_save, sender=Video, dispatch_uid="update_published_timestamp")
def update_published_timestamp(sender, instance, **kwargs):
    video = get_video_representation(instance)
    is_published = instance.state == VideoStateOptions.PUBLISHED
    if is_published and instance.published_timestamp is None:
        instance.published_timestamp = timezone.now()
        logger.info(
            f"Update 'published_timestamp' for video <{video}> to <{instance.published_timestamp}>"
        )

    if is_published and instance.published_timestamp:
        instance.is_active = True

    elif instance.is_draft:
        instance.published_timestamp = None
        instance.is_active = False


@receiver(pre_save, sender=Video, dispatch_uid="update_video_slug")
def update_video_slug(sender, instance, **kwargs):
    update_slug(instance)


@receiver(pre_save, sender=FastEditVideoProxy, dispatch_uid="update_slug_fast_edit")
def update_slug_fast_edit_model(sender, instance, **kwargs):
    update_slug(instance)


@receiver(pre_save, sender=VideoProxy, dispatch_uid="update_slug_video_proxy")
def update_slug_video_proxy(sender, instance, **kwargs):
    update_slug(instance)


@receiver(pre_save, sender=PrivateVideoProxy, dispatch_uid="update_slug_private")
def update_slug_private_video_proxy(sender, instance, **kwargs):
    update_slug(instance)


@receiver(pre_save, sender=UnlistedVideoProxy, dispatch_uid="update_slug_unlisted")
def update_slug_unlisted_video_proxy(sender, instance, **kwargs):
    update_slug(instance)


@receiver(pre_save, sender=DraftVideoProxy, dispatch_uid="update_slug_draft")
def update_slug_draft_video_proxy(sender, instance, **kwargs):
    update_slug(instance)


@receiver(pre_save, sender=NotPublishedVideoProxy, dispatch_uid="update_slug_not_published")
def update_slug_not_published_video_proxy(sender, instance, **kwargs):
    update_slug(instance)


@receiver(pre_save, sender=PublishedVideoProxy, dispatch_uid="update_slug_published")
def update_slug_published_video_proxy(sender, instance, **kwargs):
    update_slug(instance)
