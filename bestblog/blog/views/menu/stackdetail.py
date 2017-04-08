from django.shortcuts import render
from blog.models import Post, Category


def stackdetail(request, stack_slug):
    
    stack = Category.objects.get(slug=stack_slug)

    posts = Post.objects.filter(category_id=stack.id)

    return render(
            request,
            "menu/stack_detail.html",
            {
            "posts": posts,
            "stack": stack
            },
            )
