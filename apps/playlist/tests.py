from django.test import TestCase
from django.utils.text import slugify
from .models import Playlist
from apps.video.models import Video


class PlaylistTestCase(TestCase):
    def setUp(self) -> None:
        self.playlist = Playlist.objects.create(title="This Is Playlist")
        video_a = Video.objects.create(title="Video a", video_id="#id1")
        video_b = Video.objects.create(title="Video b", video_id="id#2")
        for video in [video_a, video_b]:
            video.playlist = self.playlist
            video.save()

    def test_create_playlist(self):
        self.assertEqual(Playlist.objects.all().count(), 1)

    def test_title(self):
        self.assertEqual(self.playlist.title, "This Is Playlist")

    def test_slug(self):
        slug = slugify(self.playlist.title)
        self.assertEqual(slug, self.playlist.slug)

    def test_description(self):
        self.assertEqual(self.playlist.description, None)

    def test_related_videos(self):
        qs = self.playlist.video.all()
        self.assertEqual(qs.count(), 2)
