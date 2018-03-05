from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.base import View
from apps.books import models as book_models
from apps.users import forms as user_forms


class CartDetailView(View):
    def get(self, request):
        cart = request.user.cart
        hot_books = book_models.Book.get_hot_books()
        return render(request, 'cart.html', {
            'cart': cart,
            'hot_books': hot_books,
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


class CartSettlementView(View):
    def get(self, request):
        settlement_form = user_forms.SettlementForm(user=request.user)
        return render(request, 'settlement.html', {
            'settlement_form': settlement_form,
        })
