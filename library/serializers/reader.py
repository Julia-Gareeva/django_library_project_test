from rest_framework import serializers

from library.models import Reader, Books
from library.validators import PhoneValidator


class ReaderDetailSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(validators=[PhoneValidator])

    active_books = serializers.SlugRelatedField(
        queryset=Books.objects.all(),
        many=True,
        slug_field="name"
    )

    def update(self, instance, validate_data):
        if validate_data["book"]:
            # Уменьшаем количество экземпляров книги, если книга добавляется в актив читателя.
            for book in validate_data["book"]:
                if book not in instance.book.all():
                    if book.quantity > 0:
                        book.quantity -= 1
                        book.save()
                    else:
                        raise serializers.ValidationError(f"Книга {book.name} отсутствует.")
            # Увеличиваем количество экземпляров книги, если книга удаляется из актива читателя.
            for book in instance.book.all():
                if book not in validate_data["book"]:
                    book.quantity += 1
                    book.save()
        return super().update(instance, validate_data)

    class Meta:
        model = Reader
        fields = "__all__"
