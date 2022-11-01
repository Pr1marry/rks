from django.template.defaulttags import url
from django.urls import path

from .views import TableViewSet, AlbumViewSet, ArtistViewSet

urlpatterns = [
    path('table_list', TableViewSet.as_view({'get': 'list'})),
    path('album_list', AlbumViewSet.as_view({'get': 'list'})),
    path('artist_list', ArtistViewSet.as_view({'get': 'list'})),
    # path('track_list/<int:pk>/', TrackViewSet.as_view({'get': 'get_list'})),
]
