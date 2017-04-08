from django.shortcuts import redirect
from blog.models import Post


def delete_comments(request, post_id, comment_id):
    
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    comment.delete()

    return redirect(
           post 
           )
