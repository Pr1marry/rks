from .models import Album, Artist, Track
from django.shortcuts import get_object_or_404, render
from .serializers import AlbumSerializer, ArtistSerializer, TrackSerializer, NameAlbumSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class TableViewSet(viewsets.ViewSet):
    # queryset_track = Track.objects.filter('')
    # serializer_track = TrackSerializer(queryset_track, many=True)
    # queryset_album = Album.objects.all()
    # serializer_album = AlbumSerializer(queryset_album, many=True)
    # queryset_artist = Artist.objects.all()
    # serializer_artist = ArtistSerializer(queryset_artist, many=True)
    queryset_album_name = Album.objects.values('id', 'name', 'artist', 'year')
    http_method_names = ['get', 'post']

    def list(self, request):
        list_elements_1 = []
        for el in range(len(self.queryset_album_name)):
            list_tracks = []
            first = self.queryset_album_name[el]['name']
            id_album = self.queryset_album_name[el]['id']
            queryset_track = Track.objects.filter(album=id_album).values('name')
            for i in range(len(queryset_track)):
                tr = queryset_track[i]['name']
                list_tracks.append(tr)
            # list_tracks.append(queryset_track)
            second = self.queryset_album_name[el]['year']
            element = str(first) + '[' + str(second) + ']'
            names = str(first)
            artists = self.queryset_album_name[el]['artist']

            elements = {'album': element, 'name': names,
                        'artist@name': artists, 'tracks': list_tracks}
            list_elements_1.append(elements)

        context = list_elements_1
        return Response(context, status=status.HTTP_200_OK)



def home_page(request):
    return render(request, 'table.html')
