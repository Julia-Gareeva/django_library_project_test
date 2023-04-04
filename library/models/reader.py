from django.contrib.auth.models import AbstractUser
from django.db import models

from library.models.books import Books


class Reader(AbstractUser):
    ACTIVE = "active"
    INACTIVE = "inactive"
    STATUS = [(ACTIVE, "Активный"), (INACTIVE, "Неактивный")]

    phone_number = models.BigIntegerField(verbose_name="Номер телефона", null=True)
    status = models.CharField(verbose_name="Статус", max_length=10, choices=STATUS, default=ACTIVE)
    active_books = models.ManyToManyField(Books, verbose_name="Активные книги", blank=True)
    date_of_editing = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)

    def display_books(self):
        return ', '.join([books.name for books in self.active_books.all()])

    display_books.short_description = "Активные книги"

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
