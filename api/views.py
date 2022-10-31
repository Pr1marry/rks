from .models import Album, Artist, Track
from django.shortcuts import get_object_or_404
from .serializers import AlbumSerializer, ArtistSerializer, TrackSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class TrackViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Track.objects.all()
        serializer = TrackSerializer(queryset, many=True)
        return Response(serializer.data)


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
