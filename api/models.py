from django.db import models


class Artist(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Имя артиста'
    )


class Album(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название альбома'
    )
    artist = models.ForeignKey(
        Artist,
        on_delete=models.PROTECT,
        verbose_name='Автор альбома'
    )
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска альбома'
    )

    def __str__(self):
        return str(self.name) + '[' + str(self.year) + ']'


class Track(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название трека'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.PROTECT,
        verbose_name='Название альбома в который входит трек'
    )

