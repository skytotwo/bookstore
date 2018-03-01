from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('detail/<int:book_id>/', views.DetailView.as_view(), name='detail'),
]
