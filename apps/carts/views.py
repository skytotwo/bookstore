from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.base import View
from apps.books import models as book_models


class CartDetailView(View):
    def get(self, request):
        cart = request.user.cart
        return render(request, 'cart.html', {
            'cart': cart,
        })


class CartAddView(View):
    def get(self, request, book_id):
        book = get_object_or_404(book_models.Book, id=book_id)
        request.user.cart.add(book)
        return HttpResponseRedirect(reverse('cart:detail'))


class CartRemoveView(View):
    def get(self, request, item_id):
        request.user.cart.remove(item_id)
        return HttpResponseRedirect(reverse('cart:detail'))
