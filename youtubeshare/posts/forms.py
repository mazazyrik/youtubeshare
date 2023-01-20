from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'link', 'genre')
        labels = {
            'text': 'Type something',
            'link': 'Add a link',
            'genre': 'Choose a genre'
        }
