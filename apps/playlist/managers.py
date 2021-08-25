from django.db import models


class PlaylistManager(models.Manager):
    def is_exists(self, field, value):
        query = {field + "__iexact": value}
        return super().get_queryset().filter(**query)

