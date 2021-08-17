"""
test cases for video model
"""

from django.test import TestCase
from .models import Video

video = {
    "title": "this is video",
    "description": "video desc",
    "video_id": "this is video id",
}


class VideoModelTestCase(TestCase):
    """
    test video functionality
    """

    VIDEOS_COUNT = 3
    NO_VIDEOS = 0
    UPDATED_TITLE = "updated title"

    def setUp(self) -> None:
        """
        create single video obj to test with
        :return:
        """
        for _ in range(self.VIDEOS_COUNT):
            Video.objects.create(**video)

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
        video_id = "this is video id"
        obj = self.created_video
        self.assertEqual(obj.video_id, video_id)

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
