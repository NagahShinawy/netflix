from django.contrib import admin
from .models import Developer, Task


class TaskTabularInline(admin.TabularInline):
    model = Task  # relationship many[many lines]
    extra = 5


@admin.register(Task)
class TaskModeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "developer")


@admin.register(Developer)
class DeveloperModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tasks")
    inlines = [TaskTabularInline]