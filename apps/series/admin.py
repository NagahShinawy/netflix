from django.contrib import admin
from .models import Series, Season, Episode, Developer, PM, Project
from .proxies import (
    FastEditDeveloperProxyModel,
    BackendDeveloperProxyModel,
    FrontDeveloperProxyModel,
    TeamLeadProxyModel,
)


class SeasonTabularInline(admin.TabularInline):
    model = Season
    extra = 2


class EpisodeTabularInline(admin.TabularInline):
    model = Episode
    extra = 2


@admin.register(Series)
class SeriesModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "seasons_list")
    inlines = (SeasonTabularInline,)


@admin.register(Season)
class SeasonModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    inlines = (EpisodeTabularInline,)


@admin.register(Episode)
class EpisodeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Developer)
class DeveloperModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "position", "team_lead")


@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "pm", "developers_list")


@admin.register(PM)
class PMModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "projects_list", "developers_list")


@admin.register(FastEditDeveloperProxyModel)
class FastEditDeveloperProxyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "position", "team_lead")
    list_editable = ("position", "team_lead")


@admin.register(BackendDeveloperProxyModel)
class BackendDeveloperProxyModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(FrontDeveloperProxyModel)
class FrontendDeveloperProxyModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


# todo: how to implement this
@admin.register(TeamLeadProxyModel)
class TeamLeadDeveloperProxyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "team_lead")
