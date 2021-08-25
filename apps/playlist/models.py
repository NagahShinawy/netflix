from django.db import models
# from django.utils.translation import gettext_lazy as _
from apps.core.db.models import TimestampMixin, SlugMixin, InfoMixin
from apps.core.utils.base import update_slug


class Playlist(TimestampMixin, SlugMixin, InfoMixin, models.Model):

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        update_slug(instance=self)
        return super().save(*args, **kwargs)


