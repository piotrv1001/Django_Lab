from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import News
from .forms import NewsForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    #  Retrieving an item from the database
    news = News.objects.order_by('-create_time')
    # Creating a dictionary that stores database elements under the variable news
    context = {'news': news}
    # Sending the rendered page with added elements from the database
    # elements from the context dictionary are used in the news / index.html file 
    return render(request, 'news/index.html', context)

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
        news = NewsForm(request.POST)

        # If the form - that is data sent from the POST request
        # are correct, we add an element to the database
        if news.is_valid():
            news = news.save(commit=False)
            # news.author = request.user
            news.create_time = timezone.now()
            news.last_edit_time = timezone.now()
            news.save()
            return redirect('view_news')
        # If they are not correct, we send the form back to the client
        # The autmatic validator also creates error fields which are available after
        # client side
        else:
            context = {'form': news}
            return render(request, 'news/add.html', context)
    
    # If a GET query, we send an empty form
    else:
        news = NewsForm()
        context = {'form': news}
        return render(request, 'news/add.html', context)


def get(request, id):
    # get_object_or_404 returns an item from the database
    # data with the given argument value
    # or sent an error to the client
    news = get_object_or_404(News, id=id)
    context = {'news': news}
    return render(request, 'news/view.html', context)