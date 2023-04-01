from rest_framework import serializers

from library.models import Reader, Books
from library.validators import PhoneValidator, BookNotFoundValidator, BookNotFourValidator


class ReaderSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(validators=[PhoneValidator()])

    active_books = serializers.SlugRelatedField(
        many=True,
        queryset=Books.objects.all(),
        slug_field="name",
        validators=[BookNotFoundValidator(), BookNotFourValidator()]
    )

    def create(self, validated_data):
        reader = super().create(validated_data)

        reader.set_password(reader.password)
        reader.save()
        return reader

    class Meta:
        model = Reader
        fields = "__all__"
