from django.contrib import admin
from .models import Developer, Task, Tool


class TaskTabularInline(admin.TabularInline):
    model = Task  # relationship many[many lines]
    extra = 2
    fields = ("title", "desc")


@admin.register(Task)
class TaskModeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "developer")


@admin.register(Developer)
class DeveloperModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tasks", "tools_list")
    inlines = [TaskTabularInline]


@admin.register(Tool)
class ToolModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "developers")
