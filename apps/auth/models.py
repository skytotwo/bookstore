from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    GENDER_CHOICES = (('male', '男'), ('female', '女'))
    nick_name = models.CharField(max_length=10, verbose_name='昵称', default='')
    gender = models.CharField(
        max_length=6,
        verbose_name='性别',
        choices=GENDER_CHOICES,
        default='male')
    image = models.ImageField(
        upload_to='image/%Y/%m',
        default='image/default.png',
        max_length=100,
        verbose_name='头像')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
