from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class YoutubeUserManger(UserManager):
    pass


class YoutubeUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자 목록'

    objects = YoutubeUserManger
    def __str__(self):
        return self.username
