from django.contrib import admin


from .models import Genre, Author, Book, Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'stanowisko']
    list_filter = ['stanowisko', 'data_dodania']


class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ['nazwa']

admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Stanowisko, StanowiskoAdmin)
