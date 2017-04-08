from django.shortcuts import render
from blog.models import Post


def edit_comments(request, post_id, comment_id):

    content = request.POST.get("content")

    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all
    comment = post.comment_set.get(id=comment_id)

    return render(
           request,
           "posts/update_comments.html",
           {
            "post": post,
            "comments": comments,
            "comment": comment,
           },
           )
