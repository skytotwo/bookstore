from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.utils.storage import ImageStorage


class UserProfile(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatar/%Y/%m',
        storage=ImageStorage(),
        default='avatar/1.jpg',
        verbose_name='头像')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def create_cart(self):
        from apps.carts.models import Cart
        cart = Cart()
        cart.user = self
        cart.save()


class Recipient(models.Model):
    user = models.ForeignKey(
        UserProfile,
        related_name='recipient',
        on_delete=models.CASCADE,
        verbose_name='所属用户')
    name = models.CharField(max_length=20, verbose_name='收货人')
    phone_number = models.CharField(max_length=11, verbose_name='手机号')
    region = models.CharField(verbose_name='地区')
    address = models.CharField(verbose_name='详细地址')
    zip_code = models.CharField(max_length=6, verbose_name='邮编')

    def __str__(self):
        return self.user.username
