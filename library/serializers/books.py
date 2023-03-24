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
