from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('user', index, name='user'),
    path('home', index, name='home'),
    path('update_view/<id>/', update_view, name='update_view'),
    path('create_view', create_view, name='create_view'),
    path('list_view', list_view, name='list_view'),
    path('detail_view/<id>/', detail_view, name='detail_view'),
    path('delete_view/<id>/', delete_view, name='delete_view'),

]
