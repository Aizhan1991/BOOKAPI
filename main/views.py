# from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from.models import Book

from.serializerd import BookSerializer

# Create your views here.

class BookListCreateReadAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteUpdateDerailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


