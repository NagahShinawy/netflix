from django.contrib import admin
from .models import City, Country


@admin.register(City)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")
    list_editable = ("name", "country")


@admin.register(Country)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_editable = ("name", )