from django.db import models


class PublishedVideoManager(models.Manager):

    def get_queryset(self):
        return super(PublishedVideoManager, self).get_queryset().filter(is_published=True)
