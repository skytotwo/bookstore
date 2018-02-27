from django.contrib import admin
from django.urls import path, include
from apps.manages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('auth/', include('apps.authentication.urls', namespace='auth')),
    path('user/', include('apps.users.urls', namespace='user')),
]
