from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Category 


@login_required
def new(request):
    
    stacks = Category.objects.all()
   
    return render(
            request,
            "posts/create.html",
            {"stacks": stacks},
            )

def create(request):
    
    title = request.POST.get("title")
    content = request.POST.get("content")
    category = request.POST.get("category")
    image = request.FILES.get("image")
    
    post = Post.objects.create(
            title=title,
            content=content,
            image=image,
            category=Category.objects.get(slug=category)
            )

    return redirect(
            post
            )
