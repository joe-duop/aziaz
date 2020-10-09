from django.db import models

# Create your models here.
class Album(models.Model): 
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='album_images')
    date_uploaded = models.DateField()

    def __str__(self):
        return self.title



class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    song_artist = models.CharField(max_length=250)
    song_logo = models.ImageField(upload_to='albumsong_images')
    song_audiofile = models.FileField(upload_to='album_songs')

    def __str__(self):
        return self.song_title


class Mixtape(models.Model):
    mixtape_title = models.CharField(max_length=250)
    mixtape_artist = models.CharField(max_length=250)
    mixtape_logo = models.ImageField(upload_to='Mixtape_images')
    mixtape_date_uploaded = models.DateField()
    mixtape_audiofile = models.FileField(upload_to='Mixtape_songs')

    def __str__(self):
        return self.mixtape_title


class Video(models.Model):
    Video_title = models.CharField(max_length=250)
    Video_artist = models.CharField(max_length=250)
    Video_url = models.URLField()
    Video_logo = models.ImageField(upload_to='Video_images')
    Video_date_uploaded = models.DateField()

    def __str__(self):
        return self.Video_title


class Image(models.Model):
    image_title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery_images')

    def __str__(self):
        return self.image_title

