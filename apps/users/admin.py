from django.contrib import admin
from . import models


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'avatar',
        'date_joined',
        'last_login',
    )

    ordering = ('email', )

    search_fields = (
        'username',
        'email',
    )

    list_filter = ('last_login', )


@admin.register(models.Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'phone_number',
        'region',
        'address',
        'zip_code',
    )

    ordering = ('user', )

    search_fields = (
        'user',
        'name',
        'phone_number',
    )
