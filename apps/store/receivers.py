import logging

logger = logging.getLogger(__name__)


def notify_image_receiver(instance):
    if instance.pk is None:
        obj = instance.title
    else:
        obj = f"{instance.pk}-{instance.title}"
    if not instance.image:
        logger.info(f"Image of <{obj}> is missed")
    else:
        logger.info(f"Image of <{obj}> located at <{instance.image.url}>")


def discount_price_receiver(instance):
    old_price = float(instance.price)
    if instance.offer > 0:
        instance.price = old_price - ((instance.offer / 100) * old_price)
        logger.info(
            f"Price was '{old_price}' after offer of '{instance.offer}%' becomes '{instance.price}'"
        )
    return instance
