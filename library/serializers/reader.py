from rest_framework import serializers

from library.models import Reader, Books
from library.validators import PhoneValidator
from django.db import transaction


class ReaderSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(validators=[PhoneValidator()])

    active_books = serializers.SlugRelatedField(
        many=True,
        queryset=Books.objects.all(),
        slug_field="name",
    )

    def create(self, validated_data):
        active_books = validated_data.pop("active_books", None)
        reader = Reader.objects.create(**validated_data)

        # Проверка, что добаляется не более 3 активных книг.
        if len(validated_data.get("active_books", [])) > 3:
            raise serializers.ValidationError("У читателя может быть не более 3 активных книг.")

        # Проверка, что в модели Books есть хотя бы 1 книга.
        if Books.objects.aggregate(int(sum("count_of_books")))["count_of_books__sum"] == 0:
            raise serializers.ValidationError("В библиотеке должна быть хотя бы 1 книга.")

        if active_books:
            for book_name in active_books:
                books = Books.objects.get(name=book_name)
                books.count_of_books -= 1
                books.save()

        reader.set_password(reader.password)
        reader.save()
        return reader

    @transaction.atomic
    def update(self, instance, validated_data):
        active_books = validated_data.pop('active_books', [])

        # Update reader instance
        reader = super().update(instance, validated_data)

        # Удалить книги, которых нет в active_books
        for books in instance.active_books.exclude(name__in=active_books):
            books.count_of_books += 1
            books.save()
            reader.active_books.remove(books)

        # Добавление новых книг в active_books
        for name in active_books:
            books = Books.objects.get(name=name)
            if books not in instance.active_books.all():
                books.count_of_books -= 1
                books.save()
                reader.active_books.add(books)

        return reader

    class Meta:
        model = Reader
        fields = "__all__"
