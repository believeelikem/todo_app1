from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name= "index"),
    path("about/",views.about,name= "about"),
    path("add-task/",views.create_task,name = "add_task"),
    path("task/<slug:slug>/",views.view_task,name = "view_task"),
    path("edit-task/<slug:slug>/",views.edit_task,name = "edit_task"),
    path("check-uncheck/<slug:slug>/",views.check_uncheck,name="check_uncheck"),
    path("delete-task/<slug:slug>/",views.delete_task,name="delete_task"),
    path("delete-completed/",views.delete_all_completed,name = "delete_all_completed"),
    path("profile/<str:username>",views.profile, name="profile"),
    path('crash/', views.crash)    
]