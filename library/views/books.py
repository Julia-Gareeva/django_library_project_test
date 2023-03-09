from rest_framework.viewsets import ModelViewSet

from library.models import Books
from library.serializers import BooksSerializer


class BooksView(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
