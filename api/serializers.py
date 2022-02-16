from dataclasses import fields
from rest_framework import serializers
from library.models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'isbn', 'summary', 'author', 'genre']