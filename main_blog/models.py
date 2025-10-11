from django.db import models




class Category(models.Model):
    category  = models.CharField(max_length=100,blank=False,null=False)
    
    def __str__(self):
        return self.category


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="tasks")

    
    def __str__(self):
        return self.title
      

    