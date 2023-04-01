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
    def count_books(self, val):
        if val.objects.Books.count_of_books >= 1:
            return val

    def __call__(self, count_books):
        if int(count_books) == 0:
            raise serializers.ValidationError("Данной книги нет в наличии.")


class BookNotFourValidator:
    """Валидатор для проверки максимально допустимого количества книг."""
    def __call__(self, value):
        if list(str(value)) > list(str(3)):
            raise serializers.ValidationError("Не допустимо добавление больше 3 книг.")
