from django.contrib.auth.models import User
from django.db.models.signals import pre_save, pre_delete, post_save  # Inbuilt Signals
from django.db import models
from django.utils.text import slugify

# https://dev.to/kritebh/django-signals-3i92

# signals is technique used to handle events/actions on the models


class OrderByIdMixin:
    class Meta:
        ordering = ["id"]


class Note(models.Model, OrderByIdMixin):
    title = models.CharField(max_length=30)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk}-{self.title}"


class Player(models.Model, OrderByIdMixin):
    name = models.CharField(max_length=256)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f"{self.pk}-{self.name}"


class Event(models.Model):
    action = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    instance = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.action} {self.model}"


def create_event(action, model, instance=None, user=None):
    event = Event.objects.create(action=action, model=model, instance=instance, user=user)
    return event


def save_me(sender, instance, **kwargs):
    # called before saving the obj so no 'instance.id' is None (in case obj is new/create not update)
    print(f"You Are Saving <{instance}> of <{sender}>")
    create_event(action=save_me.__name__, model=sender, instance=instance)


def delete_me(sender, instance, **kwargs):
    print(f"You are deleting <{instance}> of {sender}")
    create_event(action=delete_me.__name__, model=sender, instance=instance)


def update_slug(sender, instance, **kwargs):
    if instance.slug is None and not sender.objects.filter(name__iexact=instance.name).exists():
        instance.slug = slugify(instance.name)


# save
pre_save.connect(
    save_me, sender=Note
)  # This will trigger after the saving data into Note model
post_save.connect(save_me, sender=Player)
pre_save.connect(update_slug, sender=Player)

# delete
pre_delete.connect(receiver=delete_me, sender=Note)
pre_delete.connect(receiver=delete_me, sender=Player)
# signal 'pre_save' send signal with sender 'Note' that do tasks whenever saving obj to receiver 'save_me'

# hi I am Note model as sender need to do some tasks by receiver 'save_me' to apply something whenever saving obj

# receiver 'save_me' do tasks using data from sender 'Note' which signal happened with 'pre_save'

# pre_save.connect(delete_me, sender=None)
