from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('detail/', views.cart_detail, name='detail'),
    path('add/<int:book_id>/', views.cart_add, name='add'),
    path('minus/<int:item_id>/', views.cart_minus, name='minus'),
    path('update/<int:item_id>/<int:quantity>/', views.cart_update, name='update'),
    path('remove/<int:item_id>/', views.cart_remove, name='remove'),
    path('remove-checked/', views.remove_checked_items, name='remove-checked'),
    path('settlement/', views.cart_settlement, name='settlement'),
    path('item-checked/<str:option>/<int:item_id>/', views.item_checked, name='item-checked'),
]
