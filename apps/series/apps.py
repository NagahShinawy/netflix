from django.apps import AppConfig
from importlib import import_module


class SeriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.series"

    def ready(self):
        import_module("apps.series.signals")
