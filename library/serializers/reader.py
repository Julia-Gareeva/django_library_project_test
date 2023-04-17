from rest_framework import serializers

from library.models import Reader, Books
from library.validators import PhoneValidator


class ReaderSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(validators=[PhoneValidator()])

    active_books = serializers.SlugRelatedField(
        many=True,
        queryset=Books.objects.all(),
        slug_field="name",
    )

    @staticmethod
    def validate_active_books(value):
        if len(value) > 3:
            raise serializers.ValidationError("У читателя может быть не более 3 активных книг.")
        for book in value:
            if book.count_of_books <= 0:
                raise serializers.ValidationError(f"{book.name} отсутствует в библиотеке.")
        return value

    def create(self, validated_data):
        active_books = validated_data.pop('active_books', [])

        for book in active_books:
            book.count_of_books -= 1
            book.save()
        reader = super().create(validated_data)
        reader.active_books.set(active_books)

        reader.set_password(reader.password)
        reader.save()
        return reader

    def update(self, instance, validated_data):
        active_books = validated_data.pop('active_books', [])

        for book in instance.active_books.all():
            if book not in active_books:
                book.count_of_books += 1
                book.save()

        for book in active_books:
            if book not in instance.active_books.all():
                if book.count_of_books <= 0:
                    raise serializers.ValidationError(f"{book.name} отсутствует в библиотеке.")
                book.count_of_books -= 1
                book.save()

        reader = super().update(instance, validated_data)
        reader.active_books.set(active_books)
        return reader

    class Meta:
        model = Reader
        fields = "__all__"
