from rest_framework.viewsets import ModelViewSet

from library.models import Author
from library.serializers import AuthorSerializer


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
