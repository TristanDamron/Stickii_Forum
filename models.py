from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=1000)
    text = models.CharField(max_length=10000)
