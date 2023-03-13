from rest_framework import serializers

from library.models import Books, Author
from library.validators import NumberOfPagesValidator


class BooksSerializer(serializers.ModelSerializer):
    number_of_pages = serializers.IntegerField(validators=[NumberOfPagesValidator()])

    author = serializers.SlugRelatedField(
        many=True,
        queryset=Author.objects.all(),
        slug_field="fullname"
    )

    class Meta:
        model = Books
        fields = "__all__"
