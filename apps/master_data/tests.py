from django.test import TestCase
from .models import Country, City


class TestCountry(TestCase):

    def setUp(self) -> None:
        self.egypt = Country.objects.create(name="Egypt")

        self.cairo = City.objects.create(name="Cairo", country=self.egypt)
        self.alex = City.objects.create(name="Alex", country=self.egypt)
        self.sharm = City.objects.create(name="Sharm", country=self.egypt)

    def test_create_country(self):
        self.assertEqual(Country.objects.all().count(), 1)

    def test_country_name(self):
        self.assertEqual(self.egypt.name, "Egypt")

    def test_cities_related(self):
        cities = self.egypt.cities.all()
        self.assertEqual(cities.count(), 3)


class TestCity(TestCase):

    def setUp(self) -> None:
        self.su = Country.objects.create(name="Su Arabia")
        self.riyad = City.objects.create(name="Riyad", country=self.su)

    def test_create_city(self):
        self.assertEqual(City.objects.all().count(), 1)

    def test_city_name(self):
        self.assertEqual(self.riyad.name, "Riyad")

    def test_country_of_city(self):
        self.assertEqual(self.riyad.country, self.su)

