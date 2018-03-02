import random
from django.shortcuts import render
from django.views.generic.base import View
from django.utils import timezone
from apps.books import models as book_models
from apps.manages import models as manage_models


class IndexView(View):
    def get(self, request):
        # 新书上架
        new_books = book_models.Book.objects.order_by('-added_time').all()[:10]
        # 热销推荐
        recommend_hot_books = book_models.Book.objects.order_by(
            '-sales').all()[:50]
        indexes = list(range(len(recommend_hot_books)))
        random.shuffle(indexes)
        result = []
        for i in range(len(recommend_hot_books)):
            result.append(recommend_hot_books[indexes[i]])
        recommend_hot_books = result[:10]
        # 新书热卖榜
        start = timezone.now().date() + timezone.timedelta(days=-30)
        new_hot_books = book_models.Book.objects.filter(
            added_time__gte=start).order_by('-sales').all()[:10]
        # 图书畅销榜
        hot_books = book_models.Book.objects.order_by('-sales').all()[:10]

        carousels = manage_models.Carousel.objects.order_by(
            '-added_time').all()[:5]
        categories = book_models.CategoryFirst.objects.order_by('name').all()
        return render(
            request, 'index.html', {
                'new_books': new_books,
                'recommend_hot_books': recommend_hot_books,
                'new_hot_books': new_hot_books,
                'hot_books': hot_books,
                'carousels': carousels,
                'categories': categories,
                'current_category': None,
            })
