from django.contrib import admin
from .models import Series, Season, Episode


class SeasonTabularInline(admin.TabularInline):
    model = Season
    extra = 2


class EpisodeTabularInline(admin.TabularInline):
    model = Episode
    extra = 2


@admin.register(Series)
class SeriesModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "seasons_list")
    inlines = (SeasonTabularInline, )


@admin.register(Season)
class SeasonModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    inlines = (EpisodeTabularInline, )


@admin.register(Episode)
class EpisodeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")



