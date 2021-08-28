from django.contrib import admin

from .proxy import (
    NotPublishedVideoProxy,
    DraftVideoProxy,
    UnlistedVideoProxy,
    PrivateVideoProxy,
)
from .models import Video
from .proxy import VideoProxy, FastEditVideoProxy, PublishedVideoProxy


@admin.register(Video)  # table show
class VideoModelAdmin(admin.ModelAdmin):
    date_hierarchy = "created"  # date filtration
    list_display = (
        "id",
        "video_id",
        "state",
        "title",
        "slug",
        "year",
        "playlist",
        "is_published",
        "is_active",
        "published_timestamp",
        "created",
        "updated",
    )
    list_display_links = ("id", "video_id", "title")
    list_per_page = 10

    list_editable = ("playlist",)
    list_filter = ("is_active", "state")
    search_fields = (
        "id",
        "title",
        "description",
        "playlist__title",
        "playlist__description",
    )
    readonly_fields = ["id", "is_published", "published_timestamp"]
    save_on_top = True  # btn save on top

    list_select_related = ("playlist",)

    # def active(self, video, *args, **kwargs):  # Video Model instance
    #     return video.is_published


class PublishedVideoProxyModelAdmin(admin.ModelAdmin):
    save_on_top = True


class FastEditVideoProxyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "video_id", "title", "slug", "is_published")
    list_display_links = ("id", "video_id")
    list_editable = ("title", "slug", "is_published")
    list_filter = ("title", "slug")
    list_per_page = 3

    class Meta:
        model = PublishedVideoProxy  # optional


@admin.register(PublishedVideoProxy)
class PublishedVideoProxyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


admin.site.register(VideoProxy)  # basic  video show
admin.site.register(
    FastEditVideoProxy, FastEditVideoProxyModelAdmin
)  # editable video show


class NotPublishedVideoProxyModelAdmin(admin.ModelAdmin):
    save_on_top = True

    class Meta:
        model = NotPublishedVideoProxy  # optional

    def get_queryset(self, request):
        return NotPublishedVideoProxy.objects.filter(is_active=False)


class DraftVideoProxyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    readonly_fields = ("id", "published_timestamp")

    def get_queryset(self, request):
        return DraftVideoProxy.objects.all().draft()


class UnlistedVideoProxyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    readonly_fields = ("id", "published_timestamp")

    def get_queryset(self, request):
        return DraftVideoProxy.objects.all().unlisted()


class PrivateVideoProxyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    readonly_fields = ("id", "published_timestamp")

    def get_queryset(self, request):
        return DraftVideoProxy.objects.all().private()


admin.site.register(PublishedVideoProxy, PublishedVideoProxyModelAdmin)  # basic show
admin.site.register(
    NotPublishedVideoProxy, NotPublishedVideoProxyModelAdmin
)  # basic show

admin.site.register(DraftVideoProxy, DraftVideoProxyModelAdmin)
admin.site.register(UnlistedVideoProxy, UnlistedVideoProxyModelAdmin)
admin.site.register(PrivateVideoProxy, PrivateVideoProxyModelAdmin)
# before
# admin.site.register(PublishedVideoProxy)  # basic show
# admin.site.register(NotPublishedVideoProxy)  # basic show
