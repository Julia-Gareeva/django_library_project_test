from django.urls import path
from rest_framework import routers

from library.views import (AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
                           BooksListView, BooksDetailView, BooksCreateView, BooksUpdateView, BooksDeleteView,
                           ReaderListView, ReaderDetailView, ReaderCreateView, ReaderUpdateView, ReaderDeleteView)

# Register router for DRF urls
router = routers.SimpleRouter()

urlpatterns = [
    path("author/", AuthorListView.as_view()),
    path("author/<int:pk>/", AuthorDetailView.as_view()),
    path("author/create/", AuthorCreateView.as_view()),
    path("author/update/", AuthorUpdateView.as_view()),
    path("author/delete/", AuthorDeleteView.as_view()),

    path("books/", BooksListView.as_view()),
    path("books/<int:pk>/", BooksDetailView.as_view()),
    path("books/create/", BooksCreateView.as_view()),
    path("books/update/", BooksUpdateView.as_view()),
    path("books/delete/", BooksDeleteView.as_view()),

    path("reader/", ReaderListView.as_view()),
    path("reader/<int:pk>/", ReaderDetailView.as_view()),
    path("reader/create/", ReaderCreateView.as_view()),
    path("reader/update/", ReaderUpdateView.as_view()),
    path("reader/delete/", ReaderDeleteView.as_view()),
]

urlpatterns += router.urls
