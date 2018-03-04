from django.db import models
from apps.utils.storage import ImageStorage


class Carousel(models.Model):
    image = models.ImageField(
        upload_to='carousel/%Y/%m', storage=ImageStorage(), verbose_name='轮播')
    content = models.CharField(max_length=20, verbose_name='图片内容')
    added_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

    @staticmethod
    def get_carousels(number=5):
        return Carousel.objects.order_by('-added_time').all()[:number]


class Order(models.Model):
    from apps.carts.models import CartItem
    from apps.users.models import Recipient, UserProfile
    STATE_CHOICES = (("P", "进行"), ("F", "完成"))
    user = models.ForeignKey(
        UserProfile,
        related_name='order',
        on_delete=models.CASCADE,
        verbose_name='所属用户')
    recipient = models.OneToOneField(
        Recipient,
        related_name='order',
        on_delete=models.DO_NOTHING,
        verbose_name='收货人信息')
    item = models.ForeignKey(
        CartItem,
        related_name='order',
        on_delete=models.DO_NOTHING,
        verbose_name='图书')
    payment_method = models.CharField(max_length=10, verbose_name='支付方式')
    payment_amount = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='付款金额')
    paid = models.BooleanField(verbose_name='已支付')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')
    finished_time = models.DateTimeField(verbose_name='完成时间')
    state = models.CharField(choices=STATE_CHOICES, verbose_name='状态')

    def __str__(self):
        return self.user.username

    def add_items(self, items):
        self.item = items
        self.save()
