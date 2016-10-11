from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.ForeignKey('auth.User')
    text = models.CharField(max_length=200)
    author = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)
