from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.manages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls'), name='ueditor'),
    path('', views.IndexView.as_view(), name='index'),
    path('auth/', include('apps.authentication.urls', namespace='auth')),
    path('user/', include('apps.users.urls', namespace='user')),
    path('book/', include('apps.books.urls', namespace='book')),
    path('cart/', include('apps.carts.urls', namespace='cart')),
]

# 前端显示media下的图片
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
