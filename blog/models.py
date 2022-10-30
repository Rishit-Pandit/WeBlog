from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=CASCADE)
    data_posted = models.DateTimeField(default=timezone.now)
