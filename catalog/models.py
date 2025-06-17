import uuid
from django.conf import settings
from django.db import models
from user.models import User , Author as New_Author


# Create your models here.
class Language(models.Model):
    LANGUAGE_CHOICES=(
    ("E", "ENGLISH"),
    ("Y", "YORUBA"),
    ("F", "FRENCH"),
    )
    name = models.CharField(max_length = 1, choices=LANGUAGE_CHOICES, default="E")
    def __str__(self):
        return self.name

class Genre(models.Model):
   GENRE_CHOICES = (
   ("R", "ROMANCE"),
   ("C", "COMEDY"),
   ("P", "POLITICS"),
   ("F", "FICTION"),
   )
   name = models.CharField(max_length=1,choices=GENRE_CHOICES,default="Comedy")


   def __str__(self):
       return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=11, unique = True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    author = models.ManyToManyField(New_Author,related_name="books")

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    LOAN_STATUS = (
    ("A", "AVAILABLE"),
    ("B", "BORROWED"),
    ("M", "MAINTENANCE"),
    )
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length = 1, choices = LOAN_STATUS, default = "A",unique =True)
    return_date = models.DateTimeField(blank=False, null=False)
    comments = models.TextField(blank=True, null=True)
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


