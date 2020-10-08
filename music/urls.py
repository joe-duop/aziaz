from django.urls import path
from music import views


urlpatterns = [

    path('albums/', views.albums, name='albums'),
	path('albums/<int:album_id>/', views.album_details, name='album_details'),
    path('mixtapes/', views.mixtapes, name='mixtapes'),


]