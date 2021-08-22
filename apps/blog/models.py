from django.db import models
from django.db.models.signals import pre_save, post_save, pre_init  # Inbuilt Signals

# https://dev.to/kritebh/django-signals-3i92


class OrderByIdMixin:

    class Meta:
        ordering = ["id"]


class Note(models.Model, OrderByIdMixin):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.pk}-{self.title}"


class Player(models.Model, OrderByIdMixin):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.pk}-{self.name}"


def save_me(sender, instance, **kwargs):
    # called before saving the obj so no 'instance.id' is None (in case obj is new/create not update)
    if instance.id:
        obj = f"{instance.id}-{instance}"
    else:
        obj = instance
    print(f"You Are Saving <{obj}> of <{sender}>")


def delete_me(sender, instance, **kwargs):
    print(f"You are deleting {instance} of {sender}")


def create(**kwargs):
    print("test")
    

pre_save.connect(
    save_me, sender=Note
)  # This will trigger after the saving data into Note model

pre_save.connect(save_me, sender=Player)
pre_init.connect(create, sender=Player)

# signal 'pre_save' send signal with sender 'Note' that do tasks whenever saving obj to receiver 'save_me'

# hi I am Note model as sender need to do some tasks by receiver 'save_me' to apply something whenever saving obj

# receiver 'save_me' do tasks using data from sender 'Note' which signal happened with 'pre_save'
