from django.shortcuts import render, redirect
from django.urls.base import reverse
from blog.models import Post


def index(request):

    posts = Post.objects.all()

    return render(
           request,
           "posts/index.html",
           {"posts": posts},
           )

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all

    return render(
           request,
           "posts/detail.html",
           {
           "post": post,
           "comments": comments, 
           },
           )


def new(request):
    return render(
            request,
            "posts/create.html",
            {},
            )

def create(request):
    
    title = request.POST.get("title")
    content = request.POST.get("content")
    image = request.FILES.get("image")
    
    post = Post.objects.create(
            title=title,
            content=content,
            image=image,
            )

    return redirect(post)


def edit(request, post_id):
    post_now = Post.objects.get(id=post_id)

    return render(
            request,
            "posts/update.html",
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
                "posts:index",
                )
            )
