from rest_framework import serializers

from library.models import Books, Author
from library.validators import NumberOfPagesValidator, BookNotFoundValidator


class BooksSerializer(serializers.ModelSerializer):
    number_of_pages = serializers.IntegerField(validators=[NumberOfPagesValidator])
    count_of_books = serializers.IntegerField(validators=[BookNotFoundValidator])

    author = serializers.SlugRelatedField(
        queryset=Author.objects.all(),
        many=True,
        slug_field="fullname",
    )

    class Meta:
        model = Books
        fields = "__all__"
