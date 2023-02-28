from rest_framework import serializers

from library.models import Reader, Books


class ReaderDetailSerializer(serializers.ModelSerializer):
    active_books = serializers.SlugRelatedField(
        queryset=Books.objects.all(),
        many=True, # read_only=True
        slug_field="name"
    )

    class Meta:
        model = Reader
        fields = "__all__"
