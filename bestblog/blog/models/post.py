from django.db import models
from django.urls.base import reverse


class PostManager(models.Manager):

    def public(self):
        return self.filter(is_public=True)


class Post(models.Model):

    objects = PostManager()

    title = models.CharField(verbose_name="제목", max_length=20, blank=True)
    content = models.TextField(verbose_name="본문", max_length=1000, blank=True)
    is_public = models.BooleanField(
            default=True
            )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
               "posts:detail", 
               kwargs = {"post_id" : self.id},
               )
    
    def get_update_url(self):
        return reverse(
               "posts:update",
               kwargs = {"post_id": self.id},
                )
