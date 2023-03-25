from django.db import models

from library.models.books import Books


class Reader(models.Model):
    ACTIVE = "active"
    INACTIVE = "inactive"
    STATUS = [(ACTIVE, "Активный"), (INACTIVE, "Неактивный")]

    first_name = models.CharField(verbose_name="Имя", max_length=40)
    last_name = models.CharField(verbose_name="Фамилия", max_length=40)
    phone_number = models.BigIntegerField(verbose_name="Номер телефона", null=True)
    status = models.CharField(verbose_name="Статус", max_length=10, choices=STATUS, default=ACTIVE)
    active_books = models.ManyToManyField(Books, verbose_name="Активные книги", blank=True)
    date_of_creation = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_of_editing = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
