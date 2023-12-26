from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


# Enums for fields with choices
class GenderChoices(models.TextChoices):
    MALE = 'M', _('Male')
    FEMALE = 'F', _('Female')
    OTHER = 'O', _('Other')


# Author model
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Publisher model
class Publisher(models.Model):
    publisher_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.publisher_name


# Faculty model
class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50)
    person = models.CharField(max_length=50)


# Language model
class Language(models.Model):
    language_name = models.CharField(max_length=70)

    def __str__(self):
        return self.language_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_persian = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Section(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    section_persian = models.CharField(max_length=100)

    def __str__(self):
        return self.section


# Book model
class Book(models.Model):
    signatory = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=30)
    pages = models.IntegerField()
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    edition = models.IntegerField()
    publication_year = models.IntegerField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


# EBook model (inherits from Book)
class EBook(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    extension = models.CharField(max_length=30)


# Copy model
class Copy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)


