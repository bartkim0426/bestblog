from django.shortcuts import redirect
from django.urls.base import reverse


def delete(request, post_id):

    post_now = Post.objects.get(id=post_id)
    
    post_now.delete()

    return redirect(
            reverse(
                "posts:index",
                )
            )
