from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class YoutubeUserManger(BaseUserManager):

    def create_user(
            self,
            email,
            name,
            nickname,
            password=None):
        user = self.model(
            email=email,
            name=name,
            nickname=nickname,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
            self,
            email,
            name,
            nickname,
            password):
        user = self.model(
            email=email,
            name=name,
            nickname=nickname,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class YoutubeUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name', 'nickname',)

    objects = YoutubeUserManger()

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자 목록'

    def __str__(self):
        return self.email


    def get_short_name(self):
        return self.name