from rest_framework import serializers

from library.models import Books


class BooksListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="fullname"
    )

    class Meta:
        model = Books
        fields = ["id", "name", "description", "number_of_pages", "author", "count_of_books", "date_of_creation",
                  "date_of_editing"]


class BooksDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="fullname"
    )

    class Meta:
        model = Books
        fields = "__all__"


class BooksCreateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="fullname"
    )

    class Meta:
        model = Books
        fields = ["name", "description", "number_of_pages", "author", "count_of_books"]


class BooksUpdateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="fullname"
    )

    class Meta:
        model = Books
        fields = ["name", "description", "number_of_pages", "author", "count_of_books"]


class BooksDeleteSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="fullname"
    )

    class Meta:
        model = Books
        fields = ["id", "name"]
