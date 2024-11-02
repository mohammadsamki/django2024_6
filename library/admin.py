from django.contrib import admin

from .models import Autor, Book, BookInstance, Gener, Language, Users

# Register your models here.


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('fName', 'LName', 'dateOfBirth', 'dateOfDeath')
    list_filter = ('dateOfBirth', 'dateOfDeath')
    search_fields = ['fName', 'LName']


@admin.register(Gener)
class GenerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publishDate', 'language', 'summery')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_back', 'status', 'imprint')
    list_filter = ('book',)
    search_fields = ['status']
    fieldsets = (
        (None,
         {'fields':('book', 'imprint')}),
        ('Avil',
         {'fields':('status', 'due_back')})
    )
