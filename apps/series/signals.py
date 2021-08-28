from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Developer


@receiver(pre_save, sender=Developer)
def update_team_lead(sender, instance, **kwargs):
    if instance.pk == instance.team_lead.pk:
        instance.is_tl = True
    return instance
