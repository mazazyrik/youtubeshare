from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Genre(models.Model):
    genre = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.genre


class Post(models.Model):
    link = models.URLField()
    text = models.TextField(max_length=400)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    genre = models.ForeignKey(
        Genre,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='genre_key'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
