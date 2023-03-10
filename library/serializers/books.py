from rest_framework import serializers

from library.models import Books, Author
from library.validators import NumberOfPagesValidator


class BooksSerializer(serializers.ModelSerializer):
    number_of_pages = serializers.IntegerField(validators=[NumberOfPagesValidator()])

    author = serializers.SlugRelatedField(
        many=True,
        queryset=Author.objects.all(),
        slug_field=[{"first_name", "last_name"}]
    )
    author_add = serializers.SlugRelatedField


    # def get_or_create_author(self, request, book_data):
    #     for author in book_data["book"]:
    #         author_obj, _ = Author.objects.get_or_create(name=author)
    #         self.object.Author.add(author_obj)
    #         self.message_user(request, f"Автор успешно добавлен.")

    class Meta:
        model = Books
        fields = "__all__"



# class BooksCreateSerializer(serializers.ModelSerializer):
#     number_of_pages = serializers.IntegerField(validators=[NumberOfPagesValidator()])
#
#     author = serializers.SlugRelatedField(
#         many=True,
#         queryset=Author.objects.get_or_create(),
#         slug_field="fullname",
#     )
#
#     class Meta:
#         model = Books
#         fields = "__all__"
