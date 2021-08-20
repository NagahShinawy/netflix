from django.contrib import admin

from .models import Video, PublishedVideoProxy, NotPublishedVideoProxy


@admin.register(Video)  # table show
class VideoModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'  # date filtration
    list_display = ("id", "video_id", "state", "title", "slug", "is_published", "is_active", "published_timestamp")
    list_display_links = ("id", "video_id", "title")
    list_filter = ("is_active", "state")
    readonly_fields = ["id", "is_published", "published_timestamp"]
    list_per_page = 10
    save_on_top = True  # btn save on top

    # def active(self, video, *args, **kwargs):  # Video Model instance
    #     return video.is_published


class PublishedVideoProxyModelAdmin(admin.ModelAdmin):
    save_on_top = True

    class Meta:
        model = PublishedVideoProxy  # optional

    def get_queryset(self, request):
        return PublishedVideoProxy.objects.filter(is_active=True)


class NotPublishedVideoProxyModelAdmin(admin.ModelAdmin):
    save_on_top = True

    class Meta:
        model = NotPublishedVideoProxy  # optional

    def get_queryset(self, request):
        return NotPublishedVideoProxy.objects.filter(is_active=False)


admin.site.register(PublishedVideoProxy, PublishedVideoProxyModelAdmin)  # basic show
admin.site.register(
    NotPublishedVideoProxy, NotPublishedVideoProxyModelAdmin
)  # basic show

# before
# admin.site.register(PublishedVideoProxy)  # basic show
# admin.site.register(NotPublishedVideoProxy)  # basic show
