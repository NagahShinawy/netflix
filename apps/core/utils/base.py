import logging
from django.utils.text import slugify

logger = logging.getLogger(__name__)


def get_obj_representation(instance):
    obj = f"{instance.id}-{instance.title}" if instance.id else instance.title
    return obj


def update_slug(instance):
    obj = get_obj_representation(instance)
    if instance.slug is None:
        instance.slug = slugify(instance.title)
        logger.info(
            f"Update 'slug' for <{instance.__class__.__name__}> from <{obj}> to <{instance.slug}>"
        )
    return instance
