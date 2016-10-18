from django.db import models


class VideoCategory(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Video(models.Model):
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)
    ubloader = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
