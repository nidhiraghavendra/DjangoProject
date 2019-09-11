from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# importing to perform abstract ways of login and authentication
from django.contrib.auth import login, authenticate
# Forms in django
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    # This is triggered from URLs 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # takes in the data
        #check for validation - built in serialiser
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1') # confirms twice
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
        # send the form if it is a GET request
    return render(request, 'users/registration.html', {'form': form})
