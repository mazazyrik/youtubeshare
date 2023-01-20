from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .common import get_page_obj
from .forms import PostForm
from .models import Genre, Post

NUM_POST = 2


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:NUM_POST]
    page_obj = get_page_obj(request, posts)
    context = {
        'posts': posts,
        'page_obj': page_obj
    }
    return render(request, template, context)


def genres(request, slug):
    template = 'posts/genres.html'
    genres = get_object_or_404(Genre, slug=slug)
    posts = Post.objects.filter(
        genre=genres
    )
    page_obj = get_page_obj(request, posts)
    context = {
        'page_obj': page_obj,
        'posts': posts,
        'genre': genres,
    }
    return render(request, template, context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', post.author)  # поменять редирект
        return render(request, 'posts/create_post.html', {'form': form})
    return render(request, 'posts/create_post.html', {'form': form})
