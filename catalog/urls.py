from xml.etree.ElementInclude import include
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),

    # we use <int:pk> to capture the book id, which must be a specifically formatted string as pass it to the view as a parameter named pk (primary key).
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]