from django.urls import path

from . import views

urlpatterns = [
    path('track_list', views.TrackViewSet.as_view({'get': 'list'})),
    path('album_list', views.AlbumViewSet.as_view({'get': 'list'})),
    path('artist_list', views.ArtistViewSet.as_view({'get': 'list'})),
]
