from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from . import models as user_models


class OrderCreateView(View):
    def get(self, request):
        user = request.user
        user_models.Order.create(
            user=user,
            recipient=user.recipient.get(id=1),
            items=user.cart.get_checked_items(),
            payment_method='alipay',
            payment_amount=user.cart.get_total_price())
        return HttpResponse('success')
