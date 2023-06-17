from django import forms
from .models import Movie

# creating a form


class MovieForms(forms.ModelForm):

    # create meta class
    class Meta:

        # specify model to be used
        model = Movie

        # specify fields to be used
        fields = ['title',  'release_date', 'genre',
                  'production_company', 'director', 'movie_link', 'image']

        labels = {
            'Movie Title',
            'Release Date'
            'Genre',
            'Production Company',
            'Director',
            'Movie Link',
            'Image'
        }
