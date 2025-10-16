from django.shortcuts import render,redirect
from .models import Todo,Category
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    tasks = Todo.objects.filter(user = request.user).order_by("-created_at")
    categories = Category.objects.all()
    
    if request.method == "GET":
        search_term = request.GET.get("search")
        category_id = request.GET.get("category")
        status = request.GET.get("status")
        
        if search_term:
            tasks = tasks.filter(
                Q(title__icontains = search_term.lower()) |
                Q(description__icontains = search_term)
            )                        
        if category_id:
            tasks = tasks.filter(category_id = category_id)              
        if status:
            tasks = tasks.filter(completed = False ) if status.lower() == "pending" \
                else tasks.filter(completed = True )
                
    p = Paginator(tasks,3)
    page = request.GET.get("page")
    
    tasks = p.get_page(page)
    
    print(tasks.paginator.num_pages)
        
                    
        
    context = {
        "tasks":tasks,
        "categories":categories,
        "page":page
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
        category_id = request.POST.get("category") 
        new_category = request.POST.get("new_category")
        
        print(f" id: {category_id}, new_val: {bool(new_category)}")
        
        if new_category:
            category,created = Category.objects.get_or_create(category=new_category)
        else:
            category = Category.objects.get(id = category_id)
                       
        task = Todo.objects.create(title = title,description = description,category = category,user = request.user)
        task.save()    
        messages.success(request, "Task Created successfully!")
           
        return redirect("index")     
    categories = Category.objects.all() 
    return render(request,"add_task.html",{"categories":categories})


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