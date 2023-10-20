from django.shortcuts import render ,HttpResponse,redirect
from datetime import datetime
from django.contrib import messages

from home.models import Login

from django.contrib.auth.models import User

from django.contrib.auth import logout,authenticate

def index(request):

    return render (request,"base.html")
    

# Create your views here.


        
        
    

def dashboard(request):
    return render (request,'dashboard.html')


def login(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone') 
        desc =  request.POST.get('desc')
        print(name,email,phone,desc)
        none =Login (name=name ,email=email,phone=phone,desc=desc,date=datetime.today())

        none.save()
        
        messages.success(request, "login details saved")

        
        

    return render (request,"login.html")