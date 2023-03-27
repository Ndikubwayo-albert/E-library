from rest_framework import serializers
from .models import User

from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError


class Userserializer(serializers.ModelSerializer):             
    class Meta:
        model= User
        fields= ['id', 'email','password', 'last_login','first_name','last_name','is_active',
                 'is_staff', 'is_superuser','date_joined']
        
        extra_kwargs= {'password':{
            # 'write_only': True,
            'required': True,
        }}
        
    def create(self, validated_data):
        user= User.objects.create_user(**validated_data)
        Token.objects.create(user= user)        
        return user
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # def validate(self, attrs):
    #     email_exists= User.objects.filter(email= attrs['email']).exists()
    #     if email_exists:
    #         raise ValidationError('Email already exists')            
    #     return super().validate(attrs)
            
    # def create(self, validated_data):            
    #     password= validated_data.pop('password')
    #     user= super().create(validated_data)
    #     user.set_password(password)
    #     user.save()
    #     Token.objects.create(user= user) 
        
    #     return user
        
     