from django.shortcuts import render
from .models import Post


def index(request):
    return render(
           request,
           "post/index.html",
           {"posts": Post.objects.all()},
           )
