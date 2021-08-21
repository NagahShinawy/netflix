from django.db import models
from django.utils import timezone


class VideoQuerySet(models.QuerySet):

    def published(self):
        from apps.video.models import Video
        now = timezone.now()
        return self.filter(state=Video.VideoStateOptions.PUBLISHED, published_timestamp__lte=now)

    def draft(self):
        from apps.video.models import Video
        return self.filter(state=Video.VideoStateOptions.DRAFT)


class VideoManager(models.Manager):

    def get_queryset(self):
        return VideoQuerySet(model=self.model, using=self._db)