from rest_framework.viewsets import ModelViewSet

from library.models import Reader
from library.permissions import PermissionPolicyMixin, IsOwner
from library.serializers.reader import ReaderSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class ReaderView(PermissionPolicyMixin, ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes_per_method = {
        "list": [IsAuthenticated, IsAdminUser or IsOwner],
        "create": [AllowAny],
        "update": [IsAuthenticated, IsAdminUser or IsOwner],
        "destroy": [IsAuthenticated, IsAdminUser or IsOwner],
        "retrieve": [IsAuthenticated, IsAdminUser or IsOwner],
    }
