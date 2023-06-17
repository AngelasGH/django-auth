from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=True, blank=True,)
    release_date = models.CharField(max_length=255, null=True, blank=True,)
    genre = models.CharField(max_length=255, null=True, blank=True,)
    production_company = models.CharField(
        max_length=255, null=True, blank=True,)
    director = models.CharField(max_length=255, null=True, blank=True,)
    movie_link = models.URLField(max_length=200, null=True, blank=True,)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title


# from django.db import models
# from django.contrib.auth.models import User


# class Movie(models.Model):
#     userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     release_date = models.CharField(max_length=255)
#     director = models.CharField(max_length=255)
#     production_company = models.CharField(max_length=255)
#     image = models.ImageField(null=True, blank=True, upload_to='images/')

#     def __str__(self):
#         return self.title
