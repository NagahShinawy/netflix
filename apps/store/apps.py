from importlib import import_module
from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.store"

    def ready(self):
        from apps.store import signals

        # import_module("apps.store.signals")
