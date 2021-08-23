import datetime

from django.contrib.auth.models import User
from django.db import models


class StatusChoices(models.TextChoices):
    INVALID_CREDENTIALS = "invalid_credentials", "Invalid credentials"
    SUCCESS = "success", "Success"
    LOGOUT = "logout", "Logout"


class LoginLogoutAttempt(models.Model):
    username = models.CharField(max_length=256, verbose_name="Username")
    status = models.CharField(
        max_length=256, choices=StatusChoices.choices, verbose_name="Status"
    )
    ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="IP Address")
    login_date = models.DateTimeField(auto_now_add=True, verbose_name="Login Date")
    session_duration = models.DurationField(
        default=datetime.timedelta, verbose_name="Session duration"
    )

    class Meta:
        ordering = ["-login_date"]
        verbose_name_plural = "Login/Logout Attempt"

    def __str__(self):
        return f"{self.username} {self.login_date}"

    def get_roles_displayed(self):
        try:
            user = User.objects.get(username__iexact=self.username)

        except User.DoesNotExist:
            return "-"
        permissions = user.user_permissions.all()
        if permissions:
            return ",".join([permission.name for permission in permissions])
        return "-"
