from django.contrib import admin

from .models import LoginLogoutAttempt


@admin.register(LoginLogoutAttempt)
class LoginAttemptModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "status",
        "ip",
        "login_date",
        "get_roles_displayed",
    )
    list_filter = ("status", )
    search_fields = ("status", "get_roles_displayed", "username", "id")

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
