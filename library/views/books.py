from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, \
    UpdateAPIView

from library.models import Books
from library.serializers import BooksListSerializer, BooksDetailSerializer, BooksCreateSerializer, \
    BooksUpdateSerializer, BooksDeleteSerializer


class BooksListView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksListSerializer


class BooksDetailView(RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksDetailSerializer


class BooksCreateView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksCreateSerializer


class BooksUpdateView(UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksUpdateSerializer


class BooksDeleteView(DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksDeleteSerializer
