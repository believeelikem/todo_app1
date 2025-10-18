from django.db import models
from django.contrib.auth.models  import User
from django.utils.text import slugify


class Category(models.Model):
    category  = models.CharField(max_length=100,blank=False,null=False)
    
    def __str__(self):
        return self.category


class Todo(models.Model):
    slug = models.SlugField(unique= True,blank=True,null= True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="tasks")
    
    
    def save(self,*args,**kwargs):
        if not self.slug:
            print("Run")
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            
            while Todo.objects.filter(slug = slug):
                slug = f"{base_slug}-{counter}"
                counter += 1
                
            self.slug = slug
            
                
        super().save(*args,**kwargs)
                
    
    

    
    def __str__(self):
        return self.title
      

    