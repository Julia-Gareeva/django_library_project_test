from rest_framework import serializers

from library.models import Reader, Books
from library.validators import PhoneValidator, BookValidator


class ReaderSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(validators=[PhoneValidator()])

    active_books = serializers.SlugRelatedField(
        many=True,
        queryset=Books.objects.all(),
        slug_field="name",
        validators=[BookValidator()]
    )

    def create(self, validated_data):
        reader = super().create(validated_data)

        reader.set_password(reader.password)
        reader.save()
        return reader

    def update(self, instance, validate_data):
        if validate_data[Books.name]:
            # Уменьшаем количество экземпляров книги, если книга добавляется в актив читателя.
            for book in validate_data[Books.name]:
                if book not in instance.Books.all():
                    if book.quantity > 0:
                        book.quantity -= 1
                        book.save()
                    else:
                        raise serializers.ValidationError(f"Книга {Books.name} отсутствует.")
            # Увеличиваем количество экземпляров книги, если книга удаляется из актива читателя.
            for book in instance.Books.all():
                if book not in validate_data[Books.name]:
                    book.quantity += 1
                    book.save()
        return super().update(instance, validate_data)

    class Meta:
        model = Reader
        fields = "__all__"
