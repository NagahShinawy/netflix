from django.db import models


class CategoryChoices(models.TextChoices):
    COMEDY = "co", "Comedy"
    ROMANTIC = "ro", "Romantic"
    ACTION = "ac", "Action"
    DRAMA = "dr", "Drama"


class PositionChoices(models.TextChoices):
    UI = "ui", "Front end"
    BACKEND = "be", "Backend"
