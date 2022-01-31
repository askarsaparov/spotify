from django.db import models
from rest_framework.exceptions import ValidationError


class Song(models.Model):
    album = models.ForeignKey('music.Album', on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=150, blank=False, null=False)
    cover = models.URLField(blank=True)
    source = models.URLField(blank=False, null=False)
    listened = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
