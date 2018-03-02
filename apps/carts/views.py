from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.base import View
from apps.books import models as book_models
from .cart import Cart
from . import forms


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart.html', {
            'cart': cart,
        })


class CartUpdateView(View):
    def get(self, request, book_id):
        book = get_object_or_404(book_models.Book, id=book_id)
        cart = Cart(request)
        cart.add(book)
        return HttpResponseRedirect(reverse('cart:detail'))
