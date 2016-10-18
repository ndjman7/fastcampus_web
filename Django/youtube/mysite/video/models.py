from django.db import models


class Video(models.Model):
    kind = models.CharField(max_length=50)
    videoId = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    publishedAt = models.CharField(max_length=50)
    thumbnails = models.CharField(max_length=200)
