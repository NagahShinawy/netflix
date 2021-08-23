def get_user_ip(request):

    x_real_ip = request.META.get("HTTP_X_REAL_IP")
    if x_real_ip:
        ip = x_real_ip.split(",")[0]
    else:
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

    return ip
