from rest_framework import serializers

from library.models import Author


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name", "photo", "date_of_creation", "date_of_editing"]


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "photo"]


class AuthorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "photo"]


class AuthorDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name"]
