from django.db import models

from library.models.author import Author


class Books(models.Model):
    name = models.CharField(verbose_name="Название", max_length=60)
    description = models.TextField(verbose_name="Описание", max_length=550, null=True)
    number_of_pages = models.IntegerField(verbose_name="Количество страниц")
    author = models.ForeignKey(Author, verbose_name="Автор", max_length=200, blank=True,
                               on_delete=models.CASCADE, null=True)
    count_of_books = models.IntegerField(verbose_name="Количество книг в библиотеке")
    date_of_creation = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_of_editing = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name
