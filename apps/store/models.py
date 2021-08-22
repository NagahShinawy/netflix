from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# https://dev.to/epamindia/django-signals-30g3


class Product(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True, upload_to="products/%Y-%m-%d")
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        if self.price:
            return f"{self.title} - {self.price}$"
        return self.title


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
        print(f"Emails send to user with new product <{instance}>")


@receiver(pre_save, sender=Product)
def notify_missed_image(sender, instance, **kwargs):
    if instance.pk is None:
        obj = instance.title
    else:
        obj = f"{instance.pk}-{instance.title}"
    if not instance.image:
        print(f"Image of <{obj}> is missed")
    else:
        print(f"Image of <{obj}> located at <{instance.image.url}>")