from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogChannel(models.Model):
    channel = models.TextField(max_length=15)
    tags = models.TextField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.channel

    def __repr__(self):
        return self.channel


class BlogPost(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    votes_for = models.IntegerField(default=0)
    votes_against = models.IntegerField(default=0)
    channels = models.ForeignKey(BlogChannel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class BlogComment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

