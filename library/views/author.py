from rest_framework.viewsets import ModelViewSet

from library.models import Author
from library.permissions import PermissionPolicyMixin
from library.serializers import AuthorSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes_per_method = { PermissionPolicyMixin
    #     "list": [AllowAny],
    #     "create": [IsAuthenticated or IsAdminUser],
    #     "update": [IsAuthenticated or IsAdminUser],
    #     "destroy": [IsAuthenticated or IsAdminUser],
    #     "retrieve": [AllowAny],
    # }
