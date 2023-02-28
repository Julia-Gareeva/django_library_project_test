from rest_framework.viewsets import ModelViewSet

from library.models import Books
from library.serializers import BooksDetailSerializer


class BooksAllView(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksDetailSerializer
