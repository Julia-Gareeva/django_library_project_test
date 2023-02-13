from django.contrib import admin

from library.models import Author, Books, Reader

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Reader)
