from django.shortcuts import render, redirect
from blog.models import Post, Category


def edit(request, post_id):

    stacks = Category.objects.all()
    post_now = Post.objects.get(id=post_id)

    return render(
            request,
            "posts/update.html",
            {
        "post": post_now,
        "stacks": stacks,
            }
            )

def update(request, post_id):

    post_now = Post.objects.get(id=post_id)
    
    title = request.POST.get("title")
    content = request.POST.get("content")
    category = Category.objects.get(slug=request.POST.get("category"))

    post_now.title = title
    post_now.content = content
    post_now.category = category 
    
    post_now.save()

    return redirect(post_now)
