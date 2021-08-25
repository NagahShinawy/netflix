from django.db import models


class NameMixin(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Country(NameMixin, models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name = "Country"  # add
        verbose_name_plural = "Countries"  #


class City(NameMixin, models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="cities"
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "City"  # add
        verbose_name_plural = "Cities"  #


# eg = Country.objects.get(name="Egypt")  # one
# eg.city_set.all()  # many ==> means list all many (cities) related to country Egypt(one)
