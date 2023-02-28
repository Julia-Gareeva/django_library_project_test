from rest_framework.viewsets import ModelViewSet

from library.models import Reader
from library.serializers import ReaderDetailSerializer


class ReaderAllView(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderDetailSerializer
