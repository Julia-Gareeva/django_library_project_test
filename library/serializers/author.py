from rest_framework import serializers

from library.models import Author


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
