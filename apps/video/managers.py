from django.db import models
from django.utils import timezone
from .choices import VideoStateOptions


class VideoQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            state=VideoStateOptions.PUBLISHED, published_timestamp__lte=now
        )

    def draft(self):
        return self.filter(state=VideoStateOptions.DRAFT)

    def unlisted(self):
        return self.filter(state=VideoStateOptions.UNLISTED)

    def private(self):
        return self.filter(state=VideoStateOptions.PRIVATE)

    def is_title_exists(self, title):
        return self.filter(title__iexact=title).exists()


class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(model=self.model, using=self._db)

    # you can get published directly with manager or using qs
    # 1- using manager  => Video.objects.published()
    # 2- using Queryset ==> Video.objects.all().published()
    def published(self):
        return self.get_queryset().published()

    def is_title_exists(self, title):
        return self.get_queryset().is_title_exists(title)
