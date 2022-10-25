from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def log_in(request):
    # Checking if the user is logged in
    # If so - redirect him to the page with the message list
    if request.user.is_authenticated:
        return redirect('view_news')

    # Checking what type of HTTP request is
    # If POST - user login attempt
    if request.method == 'POST':

        # Using the form to check if all data has been entered
        form = LoginForm(request.POST)
        if form.is_valid():

            # Using the built-in authentication system in Django 
            # to check if the user exists in the database
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            # If the user exists - log him in
            # and redirects to the news page
            if user is not None:
                login(request, user)
                return redirect('view_news')

            
        # If it does not exist or the transferred data is incomplete - sending
        # to the customer back the form with the data
            else:
                context = {'form': form}
                return render(request, 'authentication/login.html', context)   
        else:
            context = {'form': form}
            return render(request, 'authentication/login.html', context)
        

    # If GET is a blank form submission
    else:    
        context = {'form': LoginForm()}
        return render(request, 'authentication/login.html', context)


def log_out(request):
    logout(request)
    context = {'form': LoginForm()}
    return render(request, 'authentication/login.html', context)
    