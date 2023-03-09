# Generated by Django 4.0.1 on 2023-03-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('photo', models.ImageField(blank=True, max_length=110, upload_to='images/', verbose_name='Фото')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_of_editing', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('description', models.TextField(max_length=550, null=True, verbose_name='Описание')),
                ('number_of_pages', models.IntegerField(verbose_name='Количество страниц')),
                ('count_of_books', models.IntegerField(verbose_name='Количество книг в библиотеке')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_of_editing', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('author', models.ManyToManyField(max_length=200, to='library.Author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('phone_number', models.BigIntegerField(null=True, verbose_name='Номер телефона')),
                ('status', models.CharField(choices=[('active', 'Активный'), ('inactive', 'Неактивный')], default='active', max_length=10, verbose_name='Статус')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_of_editing', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('active_books', models.ManyToManyField(blank=True, to='library.Books', verbose_name='Активные книги')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
            },
        ),
    ]
