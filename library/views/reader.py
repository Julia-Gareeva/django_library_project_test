from rest_framework.viewsets import ModelViewSet

from library.models import Reader
from library.serializers.reader import ReaderSerializer


class ReaderView(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
