from django.db import models
from django.contrib.auth.hashers import make_password


class UserProfile(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    passwd = models.CharField(max_length=100, verbose_name='口令')
    email = models.CharField(max_length=50, unique=True, verbose_name='邮箱')
    photo = models.CharField(max_length=120, verbose_name='头像', blank=True,null=True)


