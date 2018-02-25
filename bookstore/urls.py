from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls', namespace='auth')),
    path('users/', include('apps.users.urls', namespace='users')),
]
