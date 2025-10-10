from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages



def index(request):
    tasks = Todo.objects.all().order_by("-created_at")
    context = {
        "tasks":tasks
    }
    return render(request,"index.html",context)

def view_task(request,id):
    task = Todo.objects.get(id = id)
    context = {
        "task":task
    }    
    return render(request,"view_task.html",context)

def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")       
                
        task = Todo.objects.create(title = title,description = description)
        task.save()    
        messages.success(request, "Task Created successfully!")   
        return redirect("index")      
    return render(request,"add_task.html")

def edit_task(request,id):
    task = Todo.objects.get(id = id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        
        task.title = title
        task.description = description       
        task.save()       
        messages.success(request, "Task updated successfully!")
        return redirect("index")
    context = {
        'task':task
    }      
    return render(request,"edit_task.html",context)

def check_uncheck(request,id):
    task = Todo.objects.get(id = id)
    
    if not task.completed:
        task.completed = True
    else:
        task.completed = False
    task.save()
    return redirect("index")

def delete_task(request,id):
    task = Todo.objects.get(id= id)
    task.delete()
    messages.warning(request, f" '{task.title}' deleted successfully")
    return redirect("index")
    
def delete_all_completed(request):
    tasks = Todo.objects.filter(completed = True)
    for task in tasks:
        task.delete()
    return redirect("index")


def about(request):
    return render(request,"about.html")