from django.db import models
from apps.video.choices import VideoStateOptions


class PublishedVideoManager(models.Manager):

    def get_queryset(self):
        return super(PublishedVideoManager, self).get_queryset().filter(state=VideoStateOptions.PUBLISHED)
