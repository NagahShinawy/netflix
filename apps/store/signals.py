import logging
import os
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from .receivers import notify_image_receiver
from .models import Product


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Product)
def create_product(sender, instance, **kwargs):
    """
    post_save signal sends other user useful argument called created
    which is useful to understand if the object is being created or updated.
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    if kwargs.get("created"):  # True just for first time when obj created
        logger.info(f"Emails send to user with new product <{instance}>")


@receiver(pre_save, sender=Product)
def notify_missed_image(sender, instance, **kwargs):
    notify_image_receiver(instance=instance)


@receiver(pre_save, sender=Product)
def dropped_price(sender, instance, **kwargs):
    if instance.id is None:
        return

    current_instance = instance
    saved_instance = sender.objects.get(id=instance.id)
    if saved_instance.price < current_instance.price:
        logger.info(
            f"You Are Changing Price From '{saved_instance.price}' to '{current_instance.price}'"
        )


@receiver(pre_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    if not instance.image:
        logger.info(f"<{instance}> was deleted")
        return
    imgpath = f"{instance.image.path}"
    os.remove(imgpath)
    logger.info(f"Image of <{instance}> at path <{imgpath}> was deleted")
