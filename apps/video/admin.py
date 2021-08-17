from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ("id", "video_id", "title", "slug")
    list_display_links = ("id", "video_id", "title")
    list_per_page = 5
