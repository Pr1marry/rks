from django.urls import path

from .views import TrackViewSet, AlbumViewSet, ArtistViewSet

urlpatterns = [
    path('track_list', TrackViewSet.as_view({'get': 'list'})),
    path('album_list', AlbumViewSet.as_view({'get': 'list'})),
    path('artist_list', ArtistViewSet.as_view({'get': 'list'})),
]
