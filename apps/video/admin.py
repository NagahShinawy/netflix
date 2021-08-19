from django.contrib import admin

from .models import Video, PublishedVideoProxy, NotPublishedVideoProxy


@admin.register(Video)  # table show
class VideoModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'  # date filtration
    list_display = ("id", "video_id", "title", "slug", "is_published")
    list_display_links = ("id", "video_id", "title")
    list_filter = ("is_active",)
    list_per_page = 3

    # @staticmethod
    # def active(video):  # Video Model instance
    #     return video.is_published


class PublishedVideoProxyModelAdmin(admin.ModelAdmin):
    class Meta:
        model = PublishedVideoProxy

    def get_queryset(self, request):
        return PublishedVideoProxy.objects.filter(is_active=True)


class NotPublishedVideoProxyModelAdmin(admin.ModelAdmin):
    class Meta:
        model = NotPublishedVideoProxy

    def get_queryset(self, request):
        return NotPublishedVideoProxy.objects.filter(is_active=False)


admin.site.register(PublishedVideoProxy, PublishedVideoProxyModelAdmin)  # basic show
admin.site.register(
    NotPublishedVideoProxy, NotPublishedVideoProxyModelAdmin
)  # basic show

# before
# admin.site.register(PublishedVideoProxy)  # basic show
# admin.site.register(NotPublishedVideoProxy)  # basic show
