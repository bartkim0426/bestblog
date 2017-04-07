from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post


def index(request):
    page = request.GET.get("page", 1)

    posts = Post.objects.all()
    
    paginator = Paginator(posts, 5)
    
    posts = paginator.page(page)

    return render(
           request,
           "posts/index.html",
           {"posts": posts},
           )
