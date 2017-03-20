from django.shortcuts import render
from .models import Post


def index(request):
    return render(
           request,
           "post/index.html",
           {"posts": Post.objects.all()},
           )

def detail(request, post_id):
    return render(
           request,
           "post/detail.html",
           {"post": Post.objects.get(id=post_id)},
           )
