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
