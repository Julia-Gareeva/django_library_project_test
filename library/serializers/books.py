from rest_framework import serializers

from library.models import Books, Author


class BooksDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=Author.objects.all(),
        many=True,
        slug_field="first_name",
    )

    class Meta:
        model = Books
        fields = "__all__"
