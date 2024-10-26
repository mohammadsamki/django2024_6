from django.contrib import admin
from .models import Users , Autor, Gener, Language, Book, BookInstance

# Register your models here.


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'country')


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('fName', 'LName', 'dateOfBirth', 'dateOfDeath')


@admin.register(Gener)
class GenerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publishDate', 'language', 'summery')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'due_back', 'status', 'imprint')
