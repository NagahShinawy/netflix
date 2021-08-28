import logging
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .receivers import discount_price_receiver


logger = logging.getLogger(__name__)

# https://dev.to/epamindia/django-signals-30g3


class Product(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank=True, upload_to="products/%Y-%m-%d")
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=1000)
    offer = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )

    def __str__(self):
        if self.price:
            return f"{self.title} - {self.price}$"
        return self.title

    def save(self, *args, **kwargs):
        instance = discount_price_receiver(self)
        return super(Product, instance).save(*args, **kwargs)
