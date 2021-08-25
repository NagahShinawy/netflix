from django.test import TestCase
from django.utils.text import slugify
from .models import Playlist


class PlaylistTestCase(TestCase):
    def setUp(self) -> None:
        self.playlist = Playlist.objects.create(title="This Is Playlist")

    def test_create_playlist(self):
        self.assertEqual(Playlist.objects.all().count(), 1)

    def test_title(self):
        self.assertEqual(self.playlist.title, "This Is Playlist")

    def test_slug(self):
        slug = slugify(self.playlist.title)
        self.assertEqual(slug, self.playlist.slug)

    def test_description(self):
        self.assertEqual(self.playlist.description, None)
