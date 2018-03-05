from django.db import models
from apps.books.models import Book


class Cart(models.Model):
    from apps.users.models import UserProfile
    user = models.OneToOneField(
        UserProfile,
        default=1,
        related_name='cart',
        on_delete=models.DO_NOTHING,
        verbose_name='所属用户')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def get_items(self):
        return self.item.all()

    def get_checked_items(self):
        return self.item.filter(checked=True).all()

    def add(self, book):
        # 购物车存在该书则+1
        items = self.get_items()
        for item in items:
            if book.id == item.book.id:
                item.quantity += 1
                item.save()
                return
        # 否则就创建
        cart_item = CartItem(book=book, cart=self, quantity=1)
        cart_item.save()
        self.save()

    def remove(self, item_id):
        items = self.get_items()
        for item in items:
            if item_id == item.id:
                item.delete()
                self.save()

    def get_total_quantity(self):
        total_quantity = 0
        items = self.get_items()
        for item in items:
            total_quantity += item.quantity
        return total_quantity

    def get_checked_total_quantity(self):
        total_quantity = 0
        items = self.get_checked_items()
        for item in items:
            total_quantity += item.quantity
        return total_quantity

    def get_total_price(self):
        total_price = 0
        items = self.get_items()
        for item in items:
            total_price += item.get_subtotal_price()
        return total_price

    def get_checked_total_price(self):
        total_price = 0
        items = self.get_checked_items()
        for item in items:
            total_price += item.get_subtotal_price()
        return total_price


class CartItem(models.Model):
    book = models.ForeignKey(
        Book, related_name='item', on_delete=models.CASCADE, verbose_name='图书')
    cart = models.ForeignKey(
        Cart,
        default=1,
        related_name='item',
        on_delete=models.CASCADE,
        verbose_name='所属购物车')
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name='数量')
    checked = models.BooleanField(default=True, verbose_name='选中')

    class Meta:
        verbose_name = '购物项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book.name

    def get_subtotal_price(self):
        return self.quantity * self.book.discount_price
