from django.contrib import admin
from . import models


@admin.register(models.Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'content',
        'added_time',
    )

    ordering = ('added_time', )

    search_fields = ('content', )

    list_filter = ('added_time', )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'recipient',
        'item',
        'payment_method',
        'payment_amount',
        'paid',
        'created_time',
        'finished_time',
        'state',
    )

    ordering = (
        'user',
        'recipient',
    )

    search_fields = ('user', )

    list_filter = ('created_time', )
