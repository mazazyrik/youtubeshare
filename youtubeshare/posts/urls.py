from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.post_create, name='post_create'),
    path('genre/<slug:slug>', views.genres, name='genres'),
]
