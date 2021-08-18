from django.contrib import admin

from .models import Video, VideoProxy, FastEditVideoProxy, PublishedVideoProxy


@admin.register(Video)  # table show
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ("id", "video_id", "title", "slug")
    list_display_links = ("id", "video_id", "title")
    list_per_page = 10


class FastEditVideoProxyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "video_id", "title", "slug", "is_published")
    list_display_links = ("id", "video_id")
    list_editable = ("title", "slug", "is_published")
    list_filter = ("title", "slug")
    list_per_page = 3


@admin.register(PublishedVideoProxy)
class PublishedVideoProxyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


admin.site.register(VideoProxy)  # basic  video show
admin.site.register(
    FastEditVideoProxy, FastEditVideoProxyModelAdmin
)  # editable video show
