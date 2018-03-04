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
    region = models.CharField(max_length=50, verbose_name='地区')
    address = models.CharField(max_length=100, verbose_name='详细地址')
    zip_code = models.CharField(max_length=6, verbose_name='邮编')

    class Meta:
        verbose_name = '收货人信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class Order(models.Model):
    from apps.carts.models import CartItem
    STATE_CHOICES = (('P', '进行'), ('F', '完成'))
    PAYMENT_METHOD_CHOICES = (('alipay', '支付宝'), ('wechat', '微信'))
    user = models.ForeignKey(
        UserProfile,
        related_name='order',
        on_delete=models.CASCADE,
        verbose_name='所属用户')
    recipient = models.ForeignKey(
        Recipient,
        related_name='order',
        on_delete=models.DO_NOTHING,
        verbose_name='收货人信息')
    item = models.ForeignKey(
        CartItem,
        related_name='order',
        on_delete=models.DO_NOTHING,
        verbose_name='图书')
    payment_method = models.CharField(
        choices=PAYMENT_METHOD_CHOICES, max_length=5, verbose_name='支付方式')
    payment_amount = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='付款金额')
    paid = models.BooleanField(default=False, verbose_name='已支付')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')
    finished_time = models.DateTimeField(
        blank=True, null=True, verbose_name='完成时间')
    state = models.CharField(
        choices=STATE_CHOICES, max_length=5, verbose_name='状态')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

    @staticmethod
    def create(user, recipient, items, payment_method, payment_amount):
        order = Order(
            user=user,
            recipient=recipient,
            payment_method=payment_method,
            payment_amount=payment_amount,
            paid=False,
            state='P')
        for item in items:
            order.item = item
        order.save()

    def add_items(self, items):
        self.item = items
        self.save()
