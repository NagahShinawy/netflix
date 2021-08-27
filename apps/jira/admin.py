from django.contrib import admin
from .models import Developer, Task


@admin.register(Developer)
class DeveloperModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tasks")


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "developer")