from django.db import models


class StateOptions(models.TextChoices):
    PUBLISHED = "PU", "PUBLISH"  # db_value, user_display_value
    DRAFT = "DR", "DRAFT"
    UNLISTED = "UN", "Unlisted"
    PRIVATE = "PR", "Private"
