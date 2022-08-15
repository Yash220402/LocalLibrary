from django.urls import include, re_path, path
from.import views
import re

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book-detail")

    # path("book/<int:pk>", views.BookDetailView.as_view(), name="book-detail")
]