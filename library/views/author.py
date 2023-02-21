from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView

from library.models import Author
from library.serializers import AuthorListSerializer, AuthorDetailSerializer, AuthorCreateSerializer, \
    AuthorUpdateSerializer, AuthorDeleteSerializer


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer


class AuthorDetailView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer


class AuthorCreateView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer


class AuthorUpdateView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorUpdateSerializer


class AuthorDeleteView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDeleteSerializer
