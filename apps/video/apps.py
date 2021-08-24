from importlib import import_module
from django.apps import AppConfig


class VideoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.video"

    def ready(self):
        import_module("apps.video.signals")
