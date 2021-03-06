from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User


class Comment(models.Model):

    user = models.ForeignKey(User, default=1)
    post = models.ForeignKey("Post")
    content = models.TextField()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse(
                "posts:detail",
                kwargs = { "post_id": self.post_id },
               ) + "#comment-" + str(self.id)
