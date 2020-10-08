from django.shortcuts import render, get_object_or_404
from music.models import Album
from music.models import AlbumSong
from music.models import Mixtape
from music.models import Video
from music.models import Image

# Create your views here.
def home(request):
	videos = Video.objects.all()
	mixtape = Mixtape.objects.all()
	return render(request, 'home.html', {'mixtape':mixtape, 'videos':videos})



def mixtapes(request):
	mixtape = Mixtape.objects.all()
	return render(request, 'mixtapes.html', {'mixtape':mixtape})



def albums(request):
	theAlbum = Album.objects.all()
	return render(request, 'albums.html', {'theAlbum':theAlbum})


def album_details(request, album_id):
	albsongs = get_object_or_404(Album, pk=album_id)
	return render(request, 'album_details.html', {'albsongs':albsongs})


def videos(request):
	videos = Video.objects.all()
	return render(request, 'videos.html', {'videos':videos})


def about(request):
	gallery = Image.objects.all()
	return render(request, 'about.html', {'gallery':gallery})


