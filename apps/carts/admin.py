from django.contrib import admin
from . import models


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', )

    ordering = ('user', )

    search_fields = ('user', )


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'cart',
        'quantity',
    )

    ordering = ('id', )

    search_fields = (
        'book',
        'cart',
    )
