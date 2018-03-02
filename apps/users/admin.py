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
