from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from apps.core.models import LoginLogoutAttempt, StatusChoices
from apps.core.utils import http


@receiver(user_logged_in, sender=User)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = http.get_user_ip(request)
    LoginLogoutAttempt.objects.create(
        username=user.username, ip=ip, status=StatusChoices.SUCCESS
    )


@receiver(user_logged_out, sender=User)
def user_logged_out_callback(sender, request, user, **kwargs):
    ip = http.get_user_ip(request)
    LoginLogoutAttempt.objects.create(
        username=user.username, ip=ip, status=StatusChoices.LOGOUT
    )


@receiver(user_login_failed, dispatch_uid="user_login_failed_callback")
def user_logged_in_failed_callback(sender, credentials, request, **kwargs):
    ip = http.get_user_ip(request)
    LoginLogoutAttempt.objects.create(
        username=credentials["username"],
        ip=ip,
        status=StatusChoices.INVALID_CREDENTIALS,
    )
