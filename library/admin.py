from django.contrib import admin
from django.db.models import QuerySet

from library.models import Author, Books, Reader


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "photo", "date_of_creation", "date_of_editing")
    # Поля которые будут показаны в админке.
    list_filter = ("first_name", "last_name", "date_of_creation")
    # Поля по которым будет производиться фильтрация в админке.
    search_fields = ("first_name", "last_name", "date_of_creation")
    # Поля по которым будет происходить поиск в админке.


class BooksAdmin(admin.ModelAdmin):
    list_display = ("name", "number_of_pages", "count_of_books", "date_of_creation",
                    "date_of_editing")
    list_filter = ("name", "number_of_pages", "author", "count_of_books")
    search_fields = ["name"]
    actions = ["change_num_books"]

    @admin.action(description="Изменить наличие книг")
    def change_num_books(self, request, queryset: QuerySet):
        for count_of_books in queryset.get("count_of_books"):
            if count_of_books >= 1:
                count = queryset.update(count_of_books=0)
                self.message_user(request, f"Значение наличия книг в библиотеке было изменено у {count} книг.")


class ReaderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "status", "date_of_creation",
                    "date_of_editing")
    list_filter = ("first_name", "last_name", "status")
    search_fields = ("first_name", "last_name")
    actions = ["status_reader"]

    @admin.action(description="Поменять статус читателя")
    def status_reader(self, request, queryset: QuerySet):
        if queryset.update(status="active"):
            count = queryset.update(status="inactive")
            self.message_user(request, f"Статус поменялся у {count} пользователей.")
        else:
            queryset.update(status="inactive")
            count = queryset.update(status="active")
            self.message_user(request, f"Статус поменялся у {count} пользователей.")

    @admin.action(description="Удалить все книги у пользователя")
    def delete_all_books(self, request, queryset: QuerySet):
        if queryset.update(active_books="name"):
            count = queryset.delete()
            self.message_user(request, f"Активные книги были удалены у {count} читателей.")


# экшены:
# метод для изменения наличия книг (установить значение 0)
# метод для удаления всех книг у пользователя

admin.site.register(Author, AuthorAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Reader, ReaderAdmin)
