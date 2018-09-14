from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('detail/', views.CartDetailView.as_view(), name='detail'),
    path('add/<int:book_id>/', views.CartAddView.as_view(), name='add'),
    path('minus/<int:item_id>/', views.CartMinusView.as_view(), name='minus'),
    path(
        'update/<int:item_id>/<int:quantity>/',
        views.CartUpdateView.as_view(),
        name='update'),
    path(
        'remove/<int:item_id>/', views.CartRemoveView.as_view(),
        name='remove'),
    path(
        'remove-checked/',
        views.RemoveCheckedItems.as_view(),
        name='remove-checked'),
    path('settlement/', views.CartSettlementView.as_view(), name='settlement'),
    path(
        'item-checked/<str:option>/<int:item_id>/',
        views.ItemCheckedView.as_view(),
        name='item-checked'),
]
