from email.policy import default
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=50)
    image = models.ImageField(default="")
    demo = models.URLField(default="")
    download = models.URLField(default="")

    def __str__(self):
        return self.title