import logging
from django.dispatch import receiver
from django.db.models.signals import pre_save
from apps.core.models import MedicalReport

logger = logging.getLogger(__name__)


@receiver(signal=pre_save,  sender=MedicalReport, dispatch_uid="update_medical_title")
def update_medical_title(sender, instance, **kwargs):
    if not instance.id:
        return 
    current_instance = instance
    old_instance = MedicalReport.objects.get(id=current_instance.pk)
    if current_instance.title != old_instance.title:
        logger.info(f"title changed from '{old_instance.title}' to '{current_instance.title}'")
        