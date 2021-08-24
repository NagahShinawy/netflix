import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from .models import Video
from .choices import VideoStateOptions


logger = logging.getLogger(__name__)


def get_video(instance):
    video = f"{instance.id}-{instance.title}" if instance.id else instance.title
    return video


@receiver(pre_save, sender=Video, dispatch_uid="update_published_timestamp")
def update_published_timestamp(sender, instance, **kwargs):
    video = get_video(instance)
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


@receiver(pre_save, sender=Video, dispatch_uid="update_slug")
def update_slug(sender, instance, **kwargs):
    video = get_video(instance)
    if instance.slug is None:
        instance.slug = slugify(instance.title)
        logger.info(
            f"Update 'slug' for video <{video}> to <{instance.slug}>"
        )

