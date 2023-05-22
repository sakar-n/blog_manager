from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Blogmodels(models.Model):
    blog_title = models.CharField(max_length=50, unique=True )
    blog_description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.blog_title
