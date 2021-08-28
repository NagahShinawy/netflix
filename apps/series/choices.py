from django.db import models


class CategoryChoices(models.TextChoices):
    COMEDY = "co", "Comedy"
    ROMANTIC = "ro", "Romantic"
    ACTION = "ac", "Action"
    DRAMA = "dr", "Drama"
