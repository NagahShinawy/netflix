from django.test import TestCase
from .models import Video

video = {
    "title": "this is video",
    "description": "video desc",
    "video_id": "this is video id"

}


class VideoModelTestCase(TestCase):

    VIDEOS_COUNT = 1
    NO_VIDEOS = 0

    def setUp(self) -> None:
        obj = Video.objects.create(**video)
        return obj

    def test_create_video(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(), self.VIDEOS_COUNT)

    def test_video_title(self):
        title = "this is video"
        obj = Video.objects.first()
        self.assertEqual(obj.title, title)

    def test_video_description(self):
        description = "video desc"
        obj = self.created_video
        self.assertEqual(obj.description, description)

    @property
    def created_video(self):
        return Video.objects.first()

    def test_video_id(self):
        video_id = "this is video id"
        obj = self.created_video
        self.assertEqual(obj.video_id, video_id)

    def test_delete_video(self):
        self.created_video.delete()
        qs = Video.objects.all()
        self.assertEqual(qs.count(), self.NO_VIDEOS)

