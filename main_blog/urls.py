from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name= "index"),
    path("add-task/",views.create_task,name = "add_task"),
    path("task/<int:id>",views.view_task,name = "view_task")
]