from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    id= models.AutoField(primary_key=True)
    title= models.CharField(max_length=150)
    author= models.CharField(max_length=50)
    # author= models.ForeignKey(User, verbose_name='Author', on_delete= models.PROTECT)
    description= models.TextField(null=True, blank=False)
    book_image= models.ImageField( upload_to='images/', null=True, default="images/default.png") 
    published_date= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title +"     by   "+self.author

# class Author(models.Model):    
#     GENDER_CHOICE = [
#         ('male','MALE'),
#         ('female','FEMALE'),
#     ]
    
#     id= models.AutoField(primary_key=True)    
#     firstname= models.CharField(max_length=500, unique=False, null=False)
#     lastname= models.CharField(max_length=500, unique=False, null=True)
#     sex= models.CharField(max_length=1500, choices= GENDER_CHOICE)
#     dateofbirth= models.DateField(auto_now=False)  
    
#     def __str__(self):
#         return self.firstname  

      
    
  
    
    
    
    
    
    