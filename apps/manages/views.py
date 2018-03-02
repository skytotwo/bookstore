from django.shortcuts import render
from django.views.generic.base import View
from apps.books import models as book_models
from apps.manages import models as manage_models


class IndexView(View):
    def get(self, request):
        new_books = book_models.Book.objects.order_by('added_time').all()[:10]
        hot_books = book_models.Book.objects.order_by('sales').all()[:10]
        carousels = manage_models.Carousel.objects.order_by(
            'added_time').all()[:5]
        categories = book_models.CategoryFirst.objects.order_by('name').all()
        return render(
            request, 'index.html', {
                'new_books': new_books,
                'hot_books': hot_books,
                'current_category': None,
                'carousels': carousels,
                'categories': categories,
            })
