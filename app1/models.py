from datetime import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class post(models.Model):
    userId=models.IntegerField()
    title=models.CharField(max_length=100)
    body=models.TextField()

    # date_posted=models.DateTimeField(default=timezone.now)
    # auth = models.ForeignKey(User,on_delete=models.CASCADE)
