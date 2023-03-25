from rest_framework import serializers

from library.models import Reader, Books
from library.validators import PhoneValidator, BookNotFoundValidator


class ReaderSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(validators=[PhoneValidator()])

    active_books = serializers.SlugRelatedField(
        many=True,
        queryset=Books.objects.all(),
        validators=[BookNotFoundValidator()],
        slug_field="name"
    )

    class Meta:
        model = Reader
        fields = "__all__"
