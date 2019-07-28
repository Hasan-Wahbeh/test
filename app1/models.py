from datetime import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class post(models.Model):
    userId=models.IntegerField()
    title=models.CharField(max_length=100)
    body=models.TextField()




class Comment(models.Model):
    user = models.CharField(max_length=200)
    email=models.EmailField()
    body = models.TextField()
    # created = models.TimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    post=models.ForeignKey(post,on_delete=models.CASCADE,default=None)
    postrelation=models.ManyToOneRel(post,on_delete=models.CASCADE,to=post,field_name="post")


