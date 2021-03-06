from django.contrib import admin
from .models import Playlist


@admin.register(Playlist)
class PlaylistModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "related_videos", "get_videos_ids", "total_videos")
    list_display_links = ("id", "slug")
    list_editable = ("title",)
    readonly_fields = ("id", "slug", "related_videos", "total_videos")
