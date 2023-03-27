from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email')
        
        email= self.normalize_email(email)
        user= self.model(email= email, **extra_fields)
        user.set_password(password)
        user.save(using= self._db )
        
        return user
    
    def create_user(self, email= None, password= None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
       
        return self._create_user(email, password, **extra_fields)
    
    def create_staffuser(self, email= None, password= None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email= None, password= None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self._create_user(email, password, **extra_fields)
             

class User(AbstractBaseUser, PermissionsMixin):
    first_name= models.CharField(max_length= 255, verbose_name= 'First name', blank= True)
    last_name= models.CharField(max_length= 255, verbose_name= 'Last name', blank= True)
    email= models.EmailField(max_length= 255, verbose_name= 'Email', unique= True) 
    password= models.CharField(max_length= 255) 
       
    is_active= models.BooleanField(default= True)
    is_staff= models.BooleanField(default= False)
    is_superuser= models.BooleanField(default= False)
        
    date_joined= models.DateTimeField(default= timezone.now)
    last_login= models.DateTimeField( null=True, blank= True)
    
    objects= CustomUserManager()    
    USERNAME_FIELD= 'email'
    EMAIL_FIELD= 'email'    
    REQUIRED_FIELDS= []
    
    class Meta:
        verbose_name= 'User'
        verbose_name_plural= 'Users'
        
    def get_full_name(self):
        return self.first_name
    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]   
    
   
