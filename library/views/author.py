from rest_framework.viewsets import ModelViewSet

from library.models import Author
from library.permissions import PermissionPolicyMixin
from library.serializers import AuthorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class AuthorView(PermissionPolicyMixin, ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes_per_method = {
        "list": [AllowAny],
        "create": [IsAuthenticated, IsAdminUser],
        "update": [IsAuthenticated, IsAdminUser],
        "destroy": [IsAuthenticated, IsAdminUser],
        "retrieve": [AllowAny],
    }
