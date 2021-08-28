from django.contrib import admin

from .models import Note, Player, Event


@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ("id", "action", "model", "instance", "created", "user")
    list_filter = ("model", "action")
    search_fields = ("id", "action", "model", "obj")

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Note)
admin.site.register(Player)
