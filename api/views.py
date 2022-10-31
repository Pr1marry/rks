from .models import Album, Artist, Track
from django.shortcuts import get_object_or_404, render
from .serializers import AlbumSerializer, ArtistSerializer, TrackSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class TrackViewSet(viewsets.ViewSet):
    queryset = Track.objects.all()
    serializer = TrackSerializer(queryset, many=True)
    http_method_names = ['get', 'post']

    def list(self, request):
        # query = request.GET.get('query', None)
        # query_set = Track.objects.filter(name=query)
        return Response(self.serializer.data,
                        status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AlbumViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Album.objects.all()
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)


class ArtistViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(serializer.data)


def home_page(request):
    return render(request, 'table.html')