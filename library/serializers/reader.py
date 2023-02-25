from rest_framework import serializers

from library.models import Reader, Books


class ReaderListSerializer(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(
        queryset=Books.objects.all(),
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Reader
        fields = ["id", "first_name", "last_name", "phone_number", "status", "active_books", "date_of_creation",
                  "date_of_editing"]


class ReaderDetailSerializer(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(
        queryset=Books.objects.all(),
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Reader
        fields = "__all__"


class ReaderCreateSerializer(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(
        queryset=Books.objects.all(),
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Reader
        fields = ["first_name", "last_name", "phone_number", "status", "active_books"]


class ReaderUpdateSerializer(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(
        queryset=Books.objects.all(),
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Reader
        fields = ["first_name", "last_name", "phone_number", "status", "active_books"]


class ReaderDeleteSerializer(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(
        queryset=Books.objects.all(),
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Reader
        fields = ["id", "first_name", "last_name"]
