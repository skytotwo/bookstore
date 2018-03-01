from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
        'shoppingcart/', views.ShoppingCartView.as_view(), name='shoppingcart'),
]
