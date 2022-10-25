from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    #  Retrieving an item from the database
    books = Book.objects.order_by('-create_time')
    # Creating a dictionary that stores database elements under the variable news
    context = {'books': books}
    # Sending the rendered page with added elements from the database
    # elements from the context dictionary are used in the news / index.html file 
    return render(request, 'books/index.html', context)

@login_required(login_url='/login/')
def add(request):
    # Checking the method of the HTTP request
    # If POST - we are looking for data in the body of the query
    # If GET - sent the form to be completed
    # (you can send data in the GET query -
    # but in this solution we do not use it)
    if request.method == 'POST':
        
        # Django forms allow you to validate data
        # so we create the form object from the query
        book = BookForm(request.POST)

        # If the form - that is data sent from the POST request
        # are correct, we add an element to the database
        if book.is_valid():
            book = book.save(commit=False)
            # news.author = request.user
            book.create_time = timezone.now()
            book.last_edit_time = timezone.now()
            book.save()
            return redirect('view_books')
        # If they are not correct, we send the form back to the client
        # The autmatic validator also creates error fields which are available after
        # client side
        else:
            context = {'form': book}
            return render(request, 'books/add.html', context)
    
    # If a GET query, we send an empty form
    else:
        book = BookForm()
        context = {'form': book}
        return render(request, 'books/add.html', context)


def get(request, id):
    # get_object_or_404 returns an item from the database
    # data with the given argument value
    # or sent an error to the client
    book = get_object_or_404(Book, id=id)
    context = {'book': book}
    return render(request, 'books/view.html', context)


@login_required(login_url='/login/')
def update(request):

    if request.method == 'POST':

        updatedbook = BookForm(request.POST)

        # If the form - that is data sent from the POST request
        # are correct, we add an element to the database
        if updatedbook.is_valid():
            updatedbook = updatedbook.save(commit=False)
            # news.author = request.user
            updatedbook.create_time = timezone.now()
            updatedbook.last_edit_time = timezone.now()
            updatedbook.save()
            return redirect('view_books')
        # If they are not correct, we send the form back to the client
        # The autmatic validator also creates error fields which are available after
        # client side
        else:
            context = {'form': book}
            return render(request, 'books/get.html', context)
    
    # If a GET query, we send an empty form
    else:
        book = BookForm()
        context = {'form': book}
        return render(request, 'books/get.html', context)