from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User


class PostManager(models.Manager):

    def public(self):
        return self.filter(is_public=True)


class Category(models.Model):
    
    slug = models.SlugField(max_length=100, unique=True)
    category = models.CharField(verbose_name="카테고리", max_length=20)
    parent_category = models.ForeignKey('self', null=True, blank=True, related_name='child')
    
    def __str__(self):
        return self.category


class Post(models.Model):

    objects = PostManager()

    user = models.ForeignKey(User, default=1)
    category = models.ForeignKey("Category", default=0)
    title = models.CharField(verbose_name="제목", max_length=20, blank=True)
    content = models.TextField(verbose_name="본문", max_length=1000, blank=True)
    image = models.ImageField(
            null=True,
            blank=True,
            )
    is_public = models.BooleanField(
            default=True
            )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
               "posts:detail", 
               kwargs = 
                   {
                "post_id": self.id,
                   },
               )
    
    def get_update_url(self):
        return reverse(
               "posts:update",
               kwargs = {"post_id": self.id},
                )

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return "http://placehold.it/300x200"
