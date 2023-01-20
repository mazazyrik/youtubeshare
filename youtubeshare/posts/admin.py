from django.contrib import admin
from .models import Genre, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'genre',
        'link',
    )
    list_editable = ('genre',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'genre',
    )
    search_fields = ('genre',)
    prepopulated_fields = {"slug": ("genre",)}
    empty_value_display = '-пусто-'


admin.site.register(Genre, GenreAdmin)
admin.site.register(Post, PostAdmin)
