"""
test cases for video model
"""

from django.utils import timezone
from django.test import TestCase
from django.utils.text import slugify
from .models import Video
from apps.playlist.models import Playlist
from .choices import VideoStateOptions

video = {"title": "this is video", "description": "video desc", "slug": "this-is-video"}


class VideoModelTestCase(TestCase):
    """
    test video functionality
    """

    VIDEOS_COUNT = 3
    NO_VIDEOS = 0
    UPDATED_TITLE = "updated title"
    DRAFT = "DR"

    def setUp(self) -> None:
        """
        create single video obj to test with
        :return:
        """
        for i in range(self.VIDEOS_COUNT):
            Video.objects.create(**video, video_id=i)

        self.last_video = Video.objects.last()
        self.playlist = Playlist.objects.create(title="Playlist#1")

        self.last_video.playlist = self.playlist

    def test_create_videos(self):
        """
        test video creation
        :return:
        """
        qs = Video.objects.all()  # # pylint: disable=C0103
        self.assertEqual(qs.count(), self.VIDEOS_COUNT)

    def test_video_title(self):
        """
        test video title
        :return:
        """
        title = "this is video"
        obj = self.created_video
        self.assertEqual(obj.title, title)

    def test_video_description(self):
        """
        test video description
        :return:
        """
        description = "video desc"
        obj = self.created_video
        self.assertEqual(obj.description, description)

    @property
    def created_video(self):
        """
        get created single video
        :return:
        """
        return Video.objects.first()

    def test_video_id(self):
        """
        test video id
        :return:
        """
        obj = self.created_video
        self.assertEqual(obj.video_id, "0")

    def test_delete_video(self):
        """
        test video deletion
        :return:
        """
        self.created_video.delete()
        qs = Video.objects.all()  # pylint: disable=C0103
        self.assertEqual(qs.count(), self.VIDEOS_COUNT - 1)

    def test_update_video(self):
        obj = self.created_video
        obj.title = self.UPDATED_TITLE
        obj.save()
        self.assertEqual(self.created_video.title, self.UPDATED_TITLE)

    def test_draft_case(self):
        """
        test for draft video case
        :return:
        """
        qs = Video.objects.filter(state=VideoStateOptions.DRAFT)
        self.assertEqual(qs.count(), self.VIDEOS_COUNT)

    def test_published_and_not_published(self):
        """
        test for published and not_published videos
        :return:
        """
        obj = Video.objects.first()
        obj.state = VideoStateOptions.PUBLISHED
        obj.save()
        published = Video.objects.filter(state=VideoStateOptions.PUBLISHED)
        not_published = Video.objects.exclude(state=VideoStateOptions.PUBLISHED)
        self.assertEqual(published.count(), 1)
        self.assertEqual(not_published.count(), self.VIDEOS_COUNT - 1)

    def test_published_timestamp(self):
        """
        test if state is PUBLISHED then update published_timestamp to now
        :return:
        """
        now = timezone.now()
        video.update({"state": VideoStateOptions.PUBLISHED})
        Video.objects.create(**video)
        qs = Video.objects.filter(
            published_timestamp__lte=now, state=VideoStateOptions.PUBLISHED
        )
        self.assertTrue(qs.exists())

    def test_slug(self):
        obj = Video.objects.first()
        test_slug = slugify(obj.title)
        self.assertEqual(test_slug, obj.slug)

    def test_published_manager(self):
        video.update({"state": VideoStateOptions.PUBLISHED})
        Video.objects.create(**video)
        published_qs = (
            Video.objects.all().published()
        )  # using custom qs 'VideoQuerySet' with method ''published in it
        published_qs2 = (
            Video.objects.published()
        )  # using custom manager 'VideoManager' with method ''published in it
        self.assertTrue(published_qs.exists())
        self.assertEqual(published_qs.count(), published_qs2.count())

    def test_draft(self):
        qs = Video.objects.all().draft()
        self.assertTrue(qs.exists())
        self.assertEqual(qs.count(), self.VIDEOS_COUNT)

    def test_playlist(self):
        self.assertEqual(self.playlist.id, self.last_video.playlist.id)
