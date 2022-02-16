from django import forms
from ..models import Books

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'isbn', 'summary']