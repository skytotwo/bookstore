from django.contrib import admin
from django.urls import path, include
from django.views import static
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static as img_static
from apps.manages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls'), name='ueditor'),
    path('', views.index, name='index'),
    path('auth/', include('apps.authentication.urls', namespace='auth')),
    path('user/', include('apps.users.urls', namespace='user')),
    path('book/', include('apps.books.urls', namespace='book')),
    path('cart/', include('apps.carts.urls', namespace='cart')),
    # 以识别静态资源和media
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^media/(?P<path>.*)$', static.serve,
        {'document_root': settings.MEDIA_ROOT}, name='media')
]

# 前端显示media下的图片
urlpatterns += img_static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 404
handler404 = views.page_not_found
