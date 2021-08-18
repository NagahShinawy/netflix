from django.contrib import admin

from .models import Video, VideoProxy, FastEditVideoProxy


@admin.register(Video)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ("id", "video_id", "title", "slug")
    list_display_links = ("id", "video_id", "title")
    list_per_page = 10


class FastEditVideoProxyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "video_id", "title", "slug")
    list_display_links = ("id", "video_id")
    list_editable = ("title", "slug")
    list_filter = ("title", "slug")
    list_per_page = 3


admin.site.register(VideoProxy)  # basic  video show
admin.site.register(
    FastEditVideoProxy, FastEditVideoProxyModelAdmin
)  # editable video show
