# dispatch_uid – A unique identifier for a signal receiver in cases where duplicate signals may be sent


from django.dispatch import receiver
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from apps.core.models import LoginLogoutAttempt, StatusChoices
from apps.core.utils import http


@receiver(user_logged_in, dispatch_uid="user_logged_in_callback")
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = http.get_user_ip(request)
    LoginLogoutAttempt.objects.create(
        username=user.username, ip=ip, status=StatusChoices.SUCCESS_LOGIN
    )


# if there are duplicated receiver, it triggers the first one or use dispatch_uid[unique identifier] for each receiver
@receiver(user_logged_in, dispatch_uid="user_logged_in_2_callback")
def user_logged_in_2_callback(sender, request, user, **kwargs):
    print("LOGIN-2")
    LoginLogoutAttempt.objects.create(
        username=user.username, status=StatusChoices.SUCCESS_LOGIN
    )


@receiver(user_logged_out, dispatch_uid="user_logged_out_callback")
def user_logged_out_callback(sender, request, user, **kwargs):
    ip = http.get_user_ip(request)
    LoginLogoutAttempt.objects.create(
        username=user.username, ip=ip, status=StatusChoices.SUCCESS_LOGOUT
    )


@receiver(user_login_failed, dispatch_uid="user_login_failed_callback")
def user_logged_in_failed_callback(sender, credentials, request, **kwargs):
    ip = http.get_user_ip(request)
    LoginLogoutAttempt.objects.create(
        username=credentials["username"],
        ip=ip,
        status=StatusChoices.INVALID_CREDENTIALS,
    )
