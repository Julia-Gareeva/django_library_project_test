from rest_framework import serializers


class PhoneValidator:
    """Валидотор для проверки номера телефона у пользователя (читателя)."""
    def __call__(self, value):
        if len(str(value)) != 11:
            raise serializers.ValidationError("В номере должно быть 11 цифр.")

        if int(list(str(value))[0]) != 7:
            raise serializers.ValidationError("Номер должен начинаться с 7.")


class NumberOfPagesValidator:
    """Валидотор для проверки правильности заполнения количества страниц."""
    def __call__(self, value):
        if int(value) < 0 and int(value) <= -1:
            raise serializers.ValidationError("Количество страниц не может быть отрицательным числом.")


class BookNotFoundValidator:
    """Валидотор проверки наличия книг в библиотеке."""
    def __call__(self, value):
        if value == 0:
            raise serializers.ValidationError("Данной книги нет в наличии.")
