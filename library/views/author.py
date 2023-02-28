from rest_framework.viewsets import ModelViewSet

from library.models import Author
from library.serializers import AuthorDetailSerializer


class AuthorAllView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
