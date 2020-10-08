from django.contrib import admin
from music.models import Album
from music.models import AlbumSong
from music.models import Mixtape
from music.models import Video
from music.models import Image

# Register your models here.
admin.site.register(Album)
admin.site.register(AlbumSong)
admin.site.register(Mixtape)
admin.site.register(Video)
admin.site.register(Image)