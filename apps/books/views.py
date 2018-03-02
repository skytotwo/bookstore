from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator
from . import models as book_models


class DetailView(View):
    def get(self, request, book_id, page):
        book = get_object_or_404(book_models.Book, pk=book_id)
        pagination = Paginator(
            book.comments.order_by('published_time').all(), 5).page(page)
        comments = pagination.object_list
        return render(request, 'detail.html', {
            'book': book,
            'comments': comments,
            'pagination': pagination,
        })


class CategoryView(View):
    def get(self, request, category_id):
        categories = book_models.CategoryFirst.objects.order_by('name').all()
        category_books = book_models.CategorySecond.objects.get(
            id=category_id).books.all()
        new_books = book_models.CategorySecond.objects.get(
            id=category_id).books.order_by('added_time').all()[:10]
        hot_books = book_models.CategorySecond.objects.get(
            id=category_id).books.order_by('sales').all()[:10]
        return render(
            request, 'category.html', {
                'categories': categories,
                'category_books': category_books,
                'new_books': new_books,
                'hot_books': hot_books,
            })
