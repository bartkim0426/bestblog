from django.shortcuts import render, redirect
from django.urls.base import reverse
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
            {},
            )

def create(request):
    
    title = request.POST.get("title")
    content = request.POST.get("content")
    
    post = Post.objects.create(
            title=title,
            content=content,
            )

    return redirect(post)


def edit(request, post_id):
    post_now = Post.objects.get(id=post_id)

    return render(
            request,
            "post/update.html",
            {"post": post_now},
            )

def update(request, post_id):
    post_now = Post.objects.get(id=post_id)
    
    title = request.POST.get("title")
    content = request.POST.get("content")

    post_now.title = title
    post_now.content = content
    
    post_now.save()

    return redirect(post_now)

            
def delete(request, post_id):
    post_now = Post.objects.get(id=post_id)
    
    post_now.delete()

    return redirect(
            reverse(
                "index",
                )
            )
