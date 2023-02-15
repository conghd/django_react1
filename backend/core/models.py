from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)

class Post(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, blank=False, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField(blank=False)