from .models import Video


class PublishedVideoProxy(Video):
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
