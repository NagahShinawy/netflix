from django.db import models


class HondaManager(models.Manager):
    HONDA = "Honda"

    def get_queryset(self):
        return super(HondaManager, self).get_queryset().filter(model__icontains=self.HONDA)