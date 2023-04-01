from rest_framework import serializers

from library.models import Books, Author
from library.validators import NumberOfPagesValidator


class BooksSerializer(serializers.ModelSerializer):
    number_of_pages = serializers.IntegerField(validators=[NumberOfPagesValidator()])

    author = serializers.SlugRelatedField(
        queryset=Author.objects.all(),
        slug_field="first_name"
    )

    class Meta:
        model = Books
        fields = "__all__"
