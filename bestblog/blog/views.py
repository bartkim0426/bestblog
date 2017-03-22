from django.shortcuts import render, redirect
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


def new(request):
    return render(
            request,
            "post/create.html",
            )

def create(request):
    
    title = request.POST.get("title")
    content = request.POST.get("content")
    
    post = Post.objects.create(
            title=title,
            content=content,
            )

    return redirect(post)
