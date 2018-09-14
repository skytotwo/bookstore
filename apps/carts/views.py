from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from . import forms as cart_forms
from apps.books import models as book_models
from apps.manages import models as manage_models


# 购物车
@login_required
def cart_detail(request):
    cart = request.user.cart
    hot_books = book_models.Book.get_hot_books()
    return render(request, 'cart.html', {
        'cart': cart,
        'hot_books': hot_books,
    })


# 添加到购物车
@login_required
def cart_add(request, book_id):
    book = get_object_or_404(book_models.Book, id=book_id)
    request.user.cart.add(book)
    return HttpResponseRedirect(reverse('cart:detail'))


# 商品减一
@login_required
def cart_minus(request, item_id):
    request.user.cart.item.get(id=item_id).minus_item()
    return HttpResponseRedirect(reverse('cart:detail'))


# 直接更改数量
@login_required
def cart_update_view(request, item_id, quantity):
    request.user.cart.item.get(id=item_id).update_quantity(
        quantity=quantity)
    return HttpResponseRedirect(reverse('cart:detail'))


# 移除商品
@login_required
class CartRemoveView(View):
    def get(self, request, item_id):
        request.user.cart.remove(item_id)
        return HttpResponseRedirect(reverse('cart:detail'))


# 结算页面
@login_required
class CartSettlementView(View):
    def get(self, request):
        settlement_form = cart_forms.SettlementForm()
        recipient = request.user.recipient.order_by('-default').all()
        cart = request.user.cart
        payment_method = manage_models.Payment.objects.all()
        return render(
            request, 'settlement.html', {
                'settlement_form': settlement_form,
                'recipient': recipient,
                'cart': cart,
                'payment_method': payment_method,
            })


# 选中商品
@login_required
class ItemCheckedView(View):
    def get(self, request, option, item_id):
        request.user.cart.item.get(id=item_id).change_checked(option=option)
        return HttpResponse('OK')


# 移除选中
@login_required
class RemoveCheckedItems(View):
    def get(self, request):
        request.user.cart.remove_checked_items()
        return HttpResponseRedirect(reverse('cart:detail'))
