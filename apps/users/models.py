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
