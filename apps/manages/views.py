import random
from django.shortcuts import render
from django.views.generic.base import View
from django.utils import timezone
from apps.books import models as book_models
from apps.manages import models as manage_models


class IndexView(View):
    def get(self, request):
        # 新书上架
        new_books = book_models.Book.get_new_books()
        # 热销推荐
        recommend_hot_books = book_models.Book.get_recommend_hot_books()
        # 新书热卖榜
        new_hot_books = book_models.Book.get_new_hot_books()
        # 图书畅销榜
        hot_books = book_models.Book.get_hot_books()
        # 轮播
        carousels = manage_models.Carousel.get_carousels()
        # 一级类别
        categories = book_models.CategoryFirst.get_category_first()
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