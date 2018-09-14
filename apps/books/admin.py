from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'author',
        'press',
        'added_time',
        'original_price',
        'stock',
        'sales',
    )

    ordering = (
        '-sales',
        '-added_time',
    )

    search_fields = (
        'name',
        'author',
    )

    list_filter = (
        'sales',
        'added_time',
        'press',
    )


@admin.register(models.CategoryFirst)
class CategoryFirstAdmin(admin.ModelAdmin):
    list_display = ('name', )

    ordering = ('name', )

    search_fields = ('name', )


@admin.register(models.CategorySecond)
class CategorySecondAdmin(admin.ModelAdmin):
    list_display = ('name', 'up')

    ordering = ('name', )

    search_fields = (
        'name',
        'up',
    )

    list_filter = ('up', )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'user',
        'score',
        'content',
        'published_time',
    )

    ordering = ('published_time', )

    search_fields = (
        'book',
        'user',
    )

    list_filter = (
        'score',
        'published_time',
    )
