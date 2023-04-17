from rest_framework.viewsets import ModelViewSet

from library.models import Books
from library.permissions import PermissionPolicyMixin
from library.serializers import BooksSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class BooksView(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes_per_method = { PermissionPolicyMixin,
    #     "list": [AllowAny],
    #     "create": [IsAuthenticated or IsAdminUser],
    #     "update": [IsAuthenticated or IsAdminUser],
    #     "destroy": [IsAuthenticated or IsAdminUser],
    #     "retrieve": [AllowAny]
    # }
