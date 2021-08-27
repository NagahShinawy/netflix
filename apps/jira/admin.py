from django.contrib import admin
from .models import Developer, Task, Tool


class TaskTabularInline(admin.TabularInline):
    model = Task  # relationship many[many lines]
    extra = 5


class ToolTabularInline(admin.TabularInline):
    # 'jira.Tool' has no ForeignKey to 'jira.Developer' fixed by 'Tool.developer.through'
    model = Tool.developer.through  # relationship many[many lines]
    extra = 5


@admin.register(Task)
class TaskModeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "developer")


@admin.register(Developer)
class DeveloperModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tasks")
    inlines = [TaskTabularInline, ToolTabularInline]


@admin.register(Tool)
class ToolModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "developers")