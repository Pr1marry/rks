from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Track, Album, Artist


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class NameAlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ('name', 'year',)
