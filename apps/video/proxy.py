from .models import Video
from apps.core.managers import PublishedVideoManager


class PublishedVideoProxy(Video):
    objects = PublishedVideoManager()

    class Meta:
        proxy = True  # not created db table. it just proxy
        verbose_name = "Video"
        verbose_name_plural = "Published Videos"


class NotPublishedVideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy
        verbose_name = "Video"
        verbose_name_plural = "Not Published Videos"


class DraftVideoProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Draft Video"
        verbose_name_plural = "Draft Videos"


class UnlistedVideoProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Unlisted Video"
        verbose_name_plural = "Unlisted Videos"


class PrivateVideoProxy(Video):
    class Meta:
        proxy = True
        verbose_name = "Private Video"
        verbose_name_plural = "Private Videos"


class FastEditVideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy [check proxy-model branch]
        ordering = ["title"]
        verbose_name = "Editable Video"  # add btn
        verbose_name_plural = "Fast Edit Videos"  # left side view


class VideoProxy(Video):
    class Meta:
        proxy = True  # not created db table. it just proxy [check proxy-model branch]
        verbose_name = "Movie Video"  # add
        verbose_name_plural = "Basic Video Title Show"  # left side show

    def __str__(self):
        return f"[{self.title}]"
