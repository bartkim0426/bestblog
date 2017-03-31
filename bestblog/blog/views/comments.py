from django.shortcuts import render, redirect
from blog.models import Post


def new_comments(request, post_id):

    content = request.POST.get("content")

    post = Post.objects.get(id=post_id)
    comment = post.comment_set.create(content=content)
    comment.save()

    return redirect(
           comment
           )
    

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


def update_comments(request, post_id, comment_id):

    content = request.POST.get("content")

    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    comment.content = content
    comment.save()

    return redirect(
           comment 
           )

def delete_comments(request, post_id, comment_id):
    
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    comment.delete()

    return redirect(
           post 
           )
