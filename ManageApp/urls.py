from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('delete', delete, name='delete'),
    path('modify', modify, name='modify'),
    path('search', search, name='search'),
]