from apps.video.models import Video
from .models import Playlist

django = Playlist.objects.create(title="django course")
movies = Playlist.objects.create(title="Movies")

models_ = Video.objects.create(title="models", playlist=django)
forms = Video.objects.create(title="forms", playlist=django)
templates = Video.objects.create(title="templates", playlist=django)
rest = Video.objects.create(title="rest", playlist=django)

# ################ ################ ################ ################ ################ ###############

leon_the_prof = Video.objects.create(
    title="Loen The Professional", video_id="#idid10101015", playlist=movies
)


def list_playlist_videos(playlist: Playlist):
    return playlist.videos.all()


def get_video_playlist(video):
    return video.playlist
