from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView

from library.models import Reader
from library.serializers import ReaderListSerializer, ReaderDetailSerializer, ReaderCreateSerializer, \
    ReaderUpdateSerializer, ReaderDeleteSerializer


class ReaderListView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderListSerializer


class ReaderDetailView(RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderDetailSerializer


class ReaderCreateView(CreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderCreateSerializer


class ReaderUpdateView(UpdateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderUpdateSerializer


class ReaderDeleteView(DestroyAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderDeleteSerializer
