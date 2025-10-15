from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .password import is_strong
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.



def register(request):
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
