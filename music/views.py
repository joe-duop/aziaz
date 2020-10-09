from django.shortcuts import render, get_object_or_404
from music.models import Album
from music.models import AlbumSong
from music.models import Mixtape
from music.models import Video
from music.models import Image

# Create your views here.
def home(request):
	videos = Video.objects.order_by('-Video_date_uploaded')[:4]
	mixtape = Mixtape.objects.order_by('-mixtape_date_uploaded')[:3]
	theAlbum = Album.objects.order_by('-date_uploaded')[:2]
	return render(request, 'home.html', {'mixtape':mixtape, 'videos':videos, 'theAlbum':theAlbum})



def mixtapes(request):
	mixtape = Mixtape.objects.order_by('-mixtape_date_uploaded')
	return render(request, 'mixtapes.html', {'mixtape':mixtape})



def albums(request):
	theAlbum = Album.objects.order_by('-date_uploaded')
	return render(request, 'albums.html', {'theAlbum':theAlbum})


def album_details(request, album_id):
	albsongs = get_object_or_404(Album, pk=album_id)
	return render(request, 'album_details.html', {'albsongs':albsongs})


def videos(request):
	videos = Video.objects.order_by('-Video_date_uploaded')
	return render(request, 'videos.html', {'videos':videos})


def about(request):
	gallery = Image.objects.all()
	return render(request, 'about.html', {'gallery':gallery})


