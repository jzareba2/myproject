# plik biblioteka/urls.py

from django.urls import path, include
from . import views
from .views import BookListView, BookDetailView

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path("books_cbv/", BookListView.as_view(), name="book-list"),
    path("books_cbv/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

]