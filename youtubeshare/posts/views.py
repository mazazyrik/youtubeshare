from django.shortcuts import render
# from .models import Post


def index(request):
    template = 'posts/index.html'
    return render(request, template)
