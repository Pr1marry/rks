from .models import Album, Artist, Track
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.response import Response


class TableViewSet(viewsets.ViewSet):
    queryset_album_name = Album.objects.values('id', 'name', 'artist', 'year')
    queryset_artist_name = Artist.objects.values('id', 'name')
    http_method_names = ['get', 'post']

    def list(self, request):
        """Sorting for name_url"""
        if request.GET.get('sort', '') == 'name':
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
                id_artist = self.queryset_album_name[el]['artist']
                queryset_artist = Artist.objects.filter(id=id_artist).values('name')
                artists = queryset_artist[0]['name']

                elements = {'album': element, 'name': names,
                            'artistname': artists, 'tracks': list_tracks}
                list_elements_1.append(elements)

            context = list_elements_1
            return Response(context, status=status.HTTP_200_OK)

        elif request.GET.get('sort', '') == 'artist':
            list_elements_1 = []
            for el in range(1, len(Artist.objects.all()) + 1):
                albums_list = self.queryset_album_name.filter(artist=el)
                for i in range(len(albums_list)):
                    artists = self.queryset_artist_name[el - 1]['name']
                    names = albums_list[i]['name']
                    id_albums = albums_list[i]['id']
                    element = str(id_albums) + '[' + str(names) + ']'
                    list_tracks = []
                    queryset_track = Track.objects.filter(album=id_albums).values('name')
                    for j in range(len(queryset_track)):
                        tr = queryset_track[j]['name']
                        list_tracks.append(tr)

                    elements = {'album': element, 'name': names,
                                'artistname': artists, 'tracks': list_tracks}
                    list_elements_1.append(elements)
            context = list_elements_1
            return Response(context, status=status.HTTP_200_OK)

        else:
            list_elements_1 = []
            for el in range(len(self.queryset_album_name)):
                list_tracks = []
                first = self.queryset_album_name[el]['name']
                id_album = self.queryset_album_name[el]['id']
                queryset_track = Track.objects.filter(album=id_album).values('name')
                for i in range(len(queryset_track)):
                    tr = queryset_track[i]['name']
                    list_tracks.append(tr)
                second = self.queryset_album_name[el]['year']
                element = str(first) + '[' + str(second) + ']'
                names = str(first)
                id_artist = self.queryset_album_name[el]['artist']
                queryset_artist = Artist.objects.filter(id=id_artist).values('name')
                artists = queryset_artist[0]['name']

                elements = {'album': element, 'name': names,
                            'artistname': artists, 'tracks': list_tracks}
                list_elements_1.append(elements)

            context = list_elements_1
            return Response(context, status=status.HTTP_200_OK)


def home_page(request):
    return render(request, 'table.html')
