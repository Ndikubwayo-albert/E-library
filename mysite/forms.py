# from .models import Book
from .models import *
from django import forms
from django.forms import ModelForm

# from django.contrib.auth.models import User



help_={
    'email':'Enter your email',
    'phone':'Enter your phone',
    'subject':'',
    'message':'',
}

class Bookform(ModelForm):    
    class Meta:
        model = Book
        fields = ('title', 'author', 'description','book_image')
        
        labels={
            'title':'', 
            'author':'',
            'description':'',
            'book_image':'Upload Book image less than 5MB'            
        }
        
        help_texts = {
            'title':'',
            'author':'', 
            'description':  ''          
        }
        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Book Title' }),
            'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Book Author' }), 
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}), 
               
        }
        
class Contactform(forms.Form):
    name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Your name'}), max_length=50, required=True)
    email= forms.EmailField(widget= forms.EmailInput(attrs={ 'class':'form-control','placeholder':'Your email'}), required=True)
    phone= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Phone(+250787423327)', 'class':'form-control'}), max_length=12, required=False)
    subject= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}),required=True )
    message= forms.CharField(widget= forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}), required=True)
    help_texts= help_
    

        
        
        
        
    
    
    