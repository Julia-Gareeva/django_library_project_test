from django.contrib import admin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.html import format_html

from library.models import Author, Books, Reader


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "photo", "date_of_creation", "date_of_editing")
    # Поля которые будут показаны в админке.
    list_filter = ("first_name", "last_name", "date_of_creation")
    # Поля по которым будет производиться фильтрация в админке.
    search_fields = ("first_name", "last_name", "date_of_creation")
    # Поля по которым будет происходить поиск в админке.


class BooksAdmin(admin.ModelAdmin):
    list_display = ("name", "number_of_pages", "author_link", "count_of_books", "date_of_creation",
                    "date_of_editing")
    list_filter = ("name", "number_of_pages", "author_link", "count_of_books")
    search_fields = ["name"]
    actions = ["change_num_books"]

    def author_link(self, obj):
        author = obj.author
        url = reverse("admin:library_author_changelist") + str(author.pk)
        return format_html(f"<a href='{url}'>{author}</a>")

    author_link.short_description = "Автор"

    @admin.action(description="Изменить наличие книг")
    def change_num_books(self, request, queryset: QuerySet):
        if queryset.update(count_of_books=int()):
            if int() >= 1:
                count = queryset.update(count_of_books=0)
                self.message_user(request, f"Значение наличия книг в библиотеке было изменено у {count} книг.")


class ReaderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "status", "display_books", "date_of_editing")
    list_filter = ("first_name", "last_name", "status")
    search_fields = ("first_name", "last_name")
    actions = ["status_reader", "delete_all_books"]

    @admin.action(description="Поменять статус читателя")
    def status_reader(self, request, queryset: QuerySet):
        if queryset.update(status="active"):
            count = queryset.update(status="inactive")
            self.message_user(request, f"Статус поменялся у {count} пользователей.")
        if queryset.update(status="inactive"):
            count = queryset.update(status="active")
            self.message_user(request, f"Статус поменялся у {count} пользователей.")

    @admin.action(description="Удалить все книги у читателя")
    def delete_all_books(self, request, queryset):
        for obj in queryset:
            obj.active_books.clear()
            self.message_user(request, "Список книг удален у пользователя/ей.")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Reader, ReaderAdmin)
