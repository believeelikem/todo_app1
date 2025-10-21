from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .password import is_strong
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login,logout,authenticate
# Create your views here.



def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        username =request.POST.get("username")
        password1 =request.POST.get("p1")
        password2 = request.POST.get("p2")
                
        if all([username,password1,password2]):
            if password1 == password2:
                
                try:                    
                    user = User.objects.get(username = username)
                except  ObjectDoesNotExist:   
                        new_user = User.objects.create_user(username = username,password=password1)
                        messages.info(request, f"User {new_user} created successfuly")
                        
                        return redirect("index")
                else:
                        messages.info(request, f"User {user} already exists")
                    
            else:
                messages.info(request,"Passwords mismatched")
        else:
            messages.info(request, " Please enter all fields ")
                    
                
        
        
    
    return render(request,'users/register.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            user = authenticate(request,username = username,password = password)
            
            if user:
                login(request,user)
                messages.info(request,f"Account logged in for {user}")
                next_url = request.GET.get("next","index")
                print(next_url)
                return redirect(next_url)
            
            else:
                messages.info(request,"Invalid User credentials")
                
            
    return render(request,"users/login.html")

def logout_view(request):
    messages.info(request,f"{request.user} succesfully logged out")
    logout(request)
    return redirect("index")