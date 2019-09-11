from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.contrib.auth.models import User 
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.

#FBV

@login_required
def index(request):
    print(request.user.username)
    print(dict(request))
    
    return render(request,'Blog/index.html',{'username':request.user.username})



