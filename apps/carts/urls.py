from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('detail/', views.CartDetailView.as_view(), name='detail'),
    path('add/<int:book_id>/', views.CartAddView.as_view(), name='add'),
    path(
        'remove/<int:item_id>', views.CartRemoveView.as_view(), name='remove'),
    path('settlement/', views.CartSettlementView.as_view(), name='settlement'),
]
