from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('validate-code', views.validate_code, name='validate-code'),
]
