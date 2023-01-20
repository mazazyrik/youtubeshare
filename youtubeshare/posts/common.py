from django.core.paginator import Paginator

NUM_POST = 10


def get_page_obj(request, posts):
    paginator = Paginator(posts, NUM_POST)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
