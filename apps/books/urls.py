from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path(
        'detail/<int:book_id>/<int:page>',
        views.DetailView.as_view(),
        name='detail'),
    path(
        'category/<int:category_id>/<int:page>',
        views.CategoryView.as_view(),
        name='category'),
]
