from django.contrib import admin
from . import models

admin.site.register([
    models.Book,
    models.Comment,
    models.CategoryFirst,
    models.CategorySecond,
])
