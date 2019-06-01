from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from read_count.models import Read_Count_father, ReadDetail
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.type_name

class Blog(models.Model, Read_Count_father):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    read_details = GenericRelation(ReadDetail)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    createTime = models.DateTimeField(auto_now_add=True)
    lastTime = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return "<Blog: %s>"%self.title

    class Meta:
        ordering = ['-createTime']



