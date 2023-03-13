from django.db import models


class Author(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=40)
    last_name = models.CharField(verbose_name="Фамилия", max_length=40)
    photo = models.ImageField(verbose_name="Фото", upload_to="images/", max_length=110, blank=True)
    date_of_creation = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_of_editing = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
