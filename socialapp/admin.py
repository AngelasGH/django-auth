from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',  'release_date', 'genre',
                    'production_company', 'director', 'movie_link', 'image')


admin.site.register(Movie, MovieAdmin)
