from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from . import models


class DetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(models.Book, pk=book_id)
        return render(request, 'detail.html', {
            'book': book,
        })
