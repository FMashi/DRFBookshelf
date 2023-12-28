from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Publisher model
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Faculty model
class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50)
    person = models.CharField(max_length=50)

class Libraries(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    content=models.TextField()
    content_persian=models.TextField()
    privacy=models.TextField()
    privacy_persian=models.TextField()
    services=models.TextField()
    services_persian=models.TextField()
    email=models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.faculty} - {self.services} - {self.email}"

# Language model
class Language(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_persian = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Section(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    section_persian = models.CharField(max_length=100)

    def __str__(self):
        return self.section


# Book model
class Book(models.Model):
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    signatory = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    isbn = models.CharField(max_length=30)
    pages = models.IntegerField()
    edition = models.IntegerField()
    publication_year = models.IntegerField()

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
    


