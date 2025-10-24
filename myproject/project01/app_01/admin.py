from django.contrib import admin


from .models import Genre, Author, Book, Osoba, Stanowisko

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Osoba)
admin.site.register(Stanowisko)
