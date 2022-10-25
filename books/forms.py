from django import forms
from .models import Book
import datetime


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'year']
