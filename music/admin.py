from django.contrib import admin
from music.models import Album, Artist, Song

admin.site.register([Artist, Album, Song])