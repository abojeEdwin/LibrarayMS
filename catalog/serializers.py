from rest_framework import serializers
from catalog.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name','email','dob']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'summary','author']
