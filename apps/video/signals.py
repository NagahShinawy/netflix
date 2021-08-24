import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Video
from .choices import VideoStateOptions


logger = logging.getLogger(__name__)


@receiver(pre_save, sender=Video, dispatch_uid="update_published_timestamp")
def update_published_timestamp(sender, instance, **kwargs):
    video = f"{instance.id}-{instance.title}" if instance.id else instance.title
    is_published = instance.state == VideoStateOptions.PUBLISHED
    if is_published and instance.published_timestamp is None:
        instance.published_timestamp = timezone.now()

    if is_published and instance.published_timestamp:
        instance.is_active = True

    elif instance.is_draft:
        instance.published_timestamp = None
        instance.is_active = False
    logger.info(
        f"Update 'published_timestamp' for video <{video}> to <{instance.published_timestamp}>"
    )


