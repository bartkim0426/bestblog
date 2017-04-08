from django.shortcuts import redirect
from blog.models import Post


def new_comments(request, post_id):

    content = request.POST.get("content")

    post = Post.objects.get(id=post_id)
    comment = post.comment_set.create(content=content)
    comment.save()

    return redirect(
           comment
           )
