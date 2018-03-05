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


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', )

    ordering = ('name', )

    search_fields = ('name', )

    list_filter = ('name', )
