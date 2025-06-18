from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book
from .serializers import BookSerializer



@api_view()
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
def greet(request,name):
    return render(request,'index.html',{'name':name})