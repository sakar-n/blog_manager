from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField 
from autoslug import AutoSlugField
# Create your models here.


class Blogmodels(models.Model):
    blog_title = models.CharField(max_length=50, unique=True )
    blog_description = RichTextUploadingField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    slug = AutoSlugField(populate_from="blog_title", unique=True , null= True, default=None)

    def __str__(self):
        return self.blog_title

    class Meta:
        ordering =["-created_at"]