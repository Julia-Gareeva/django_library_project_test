# Проект "Онлайн библиотека"

Серверная часть для приложения Онлайн библиотеки.<br> 
Имеются 3 модели.<br> 
Это модели "Читатели" (Reader); "Книги" (Books); и "Автор" (Author).
 
## Стек технологий

> - Python 3.8+
> - Django 3+ 
> - DRF 3.10+ 
> - База данных PostgreSQL 10+


## Создана учетная запись админа

> - логин: admin
> - пароль: defaultadmin

## Чтобы подключиться к базе данных выполните в терминале следующую команду:
```
docker run --name library_db -e POSTGRES_PASSWORD=defaultadmin -e POSTGRES_USER=admin -e POSTGRES_DB=library_db -p 5432:5432 -d postgres
```

Все зависимости есть в файле requirements.txt.

## Чтобы запустить проект локально:
```
1. Выполните команду: 
- pip install -r requirements.txt

2. Запустите Docker контейнер с бд:
- docker run --name library_db -e POSTGRES_PASSWORD=defaultadmin -e POSTGRES_USER=admin -e POSTGRES_DB=library_db -p 5432:5432 -d postgres

3. Создайте миграции:
- python manage.py makemigrations

4. Примените созданные миграции:
- python manage.py migrate

5. Запустите проект:
- python manage.py runserver
```
<br>
<br>
Также созданы сериализаторы на каждую из моделей. (Файлы в serializers > author.py; books.py; и reader.py)<br>
И представления на каждую из моделей. (Файлы в views > author.py; books.py; и reader.py)<br>
Добавлены урлы на каждый вид представления каждой из моделей (Author, Books, Reader).<br>

## Список доступных путей в проекте

> - admin/
> - author/
> - author/<<int:pk>>/
> - author/create/
> - author/update/<<int:pk>>/
> - author/delete/<<int:pk>>/
> - books/
> - books/<<int:pk>>/
> - books/create/
> - books/update/<<int:pk>>/
> - books/delete/<<int:pk>>/
> - reader/
> - reader/<<int:pk>>/
> - reader/create/
> - reader/update/<<int:pk>>/
> - reader/delete/<<int:pk>>/


Юлия Гареева<br>
25.02.2023