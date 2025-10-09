from django.shortcuts import render,redirect
from .models import Todo



def index(request):
    tasks = Todo.objects.all().order_by("-created_at")
    context = {
        "tasks":tasks
    }
    return render(request,"index.html",context)

def view_task(request,id):
    task = Todo.objects.get(id = id)
    
    return render(request,"view_task.html")

def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")       
                
        task = Todo.objects.create(title = title,description = description)
        task.save()       
        return redirect("index")      
    return render(request,"add_task.html")