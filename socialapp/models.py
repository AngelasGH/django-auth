from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    production_company = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title