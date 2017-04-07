from django.shortcuts import render
from blog.models import Post, Category


def stack(request):

    category = Category.objects.all()

    return render(
           request,
           "posts/stack.html",
           {"category": category,},
           )

def etc(request):
    etc_posts = Post.objects.filter(category="0")

    return render(
           request,
           "posts/etc.html",
           {"posts": etc_posts},
           )
 
def archives(request):
    return render(
           request,
           "posts/archives.html",
           {},
           )
