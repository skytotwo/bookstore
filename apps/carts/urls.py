from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('detail/', views.CartDetailView.as_view(), name='detail'),
    path('add/<int:book_id>/', views.CartUpdateView.as_view(), name='add'),
    path(
        'remove/<int:book_id>', views.CartUpdateView.as_view(), name='remove'),
]
