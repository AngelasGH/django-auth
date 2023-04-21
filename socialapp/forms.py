#import django forms
from django import forms
from .models import Movie

# creating a form
class MovieForms(forms.ModelForm):
    
     # create meta class
    class Meta:
        
        # specify model to be used
        model = Movie
        
        # specify fields to be used
        fields = ['title', 'description', 'release_date', 'director', 'production_company']