from django.contrib import admin
from .models import Playlist


@admin.register(Playlist)
class PlaylistModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug")
    readonly_fields = ("id", "slug")
