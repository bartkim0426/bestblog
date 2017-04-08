from django.shortcuts import render
from blog.models import Post


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
