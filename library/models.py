from django.db import models


# Create your models here.
class Users(models.Model):
    phone = models.DecimalField(max_digits=10, decimal_places=0, help_text="please enter 10 digit phone number")
    name = models.CharField(max_length=20, help_text="Enter your name", verbose_name="this must be your first name")
    country = models.CharField(max_length=20, default='345678', null=False, choices=[('ES', 'Spain'), ('UK', 'United Kingdom'), ('US', 'United States')])
    birthday = models.DateField(default='1990-01-01', null=False, verbose_name="date of birth")

    def __str__(self):
        return self.name


class Autor (models.Model):
    #  att : fName ,LName, date of birth, date of death
    fName = models.CharField(max_length=20, help_text="Enter your first name")
    LName = models.CharField(max_length=20, help_text="Enter your last name")
    dateOfBirth = models.DateField(null=False, verbose_name="date of birth")
    dateOfDeath = models.DateField(null=True, verbose_name="date of death", blank=True)

    #  ordaring
    class Meta:
        ordering = ['fName']

    #  always the __str__ must return a string
    def __str__(self):
        return self.fName + " " + self.LName


class Gener (models.Model):
    #  att : name
    name = models.CharField(max_length=20, help_text="Enter your genre name")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Language (models.Model):
    name = models.CharField(max_length=20, help_text="Enter your language name")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book (models.Model):
    #  att : title, author, publication date, language, genre,summery
    title = models.CharField(max_length=50, help_text="Enter your book title")
    author = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='books')

    publishDate = models.DateField(null=False, verbose_name="publication date")
    # foreingKey connect 1 - 1 > book > 1 language
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='books')
    #  gener will use many to many relationship 1 book > many gener
    gener = models.ManyToManyField(Gener, related_name='books')
    summery = models.TextField(max_length=1000, help_text="Enter your book summery")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


#  primary key :
import uuid


class BookInstance (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book instance")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, related_name='bookinstance')
    due_back = models.DateField(null=True, blank=True)

    loanStatus = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=loanStatus, blank=True, default='m', help_text='Book availability')
    imprint = models.CharField(max_length=20, blank=True, default='0', help_text='Imprent status')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
