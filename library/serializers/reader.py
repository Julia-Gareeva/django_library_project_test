from rest_framework import serializers

from library.models import Reader, Books
from library.validators import PhoneValidator


class ReaderSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(validators=[PhoneValidator])

    active_books = serializers.SlugRelatedField(
        queryset=Books.objects.all(),
        many=True,
        slug_field="name"
    )

    class Meta:
        model = Reader
        fields = "__all__"
