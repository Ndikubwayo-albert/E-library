from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import  UserRegisterForm
from django.contrib.auth import authenticate, login, logout

from rest_framework import viewsets
from .models import User
from .serializers import Userserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from rest_framework import generics
# from .models import User
from rest_framework.request import Request
# from rest_framework import mixins




# Create your views here.

def signup(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Account is created successfully!')
            return redirect('/signup')
        else:
            messages.error(request, 'Error : Not created!')
    else:
        form = UserRegisterForm()
        
    return render(request, 'createuser.html', {'form':form})

def signin(request):
    if request.method== 'POST':
        username= request.POST['username']
        passwd= request.POST['password']
        
        user= authenticate(request, email= username, password= passwd)
        if user is not None:
            login(request, user)
            return redirect ('/home')    
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('/signin')
             
    return render(request, 'signin.html', )

def signout(request):
    logout(request)
    
    return redirect('/signin')


class UserViewset(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class= Userserializer
    permission_classes= [IsAuthenticated]


class LoginApi(APIView):
    permission_classes= []
    
    def post(self, request: Request):
        email= request.data.get('email')
        passwd= request.data.get('password')
        user= authenticate(email= email, password= passwd) 
        
        if user is not None:
            response= {
                'message':'logged in successfully',
                'token': user.auth_token.key
            }
            return Response(data= response, status= status.HTTP_200_OK)
        else:
            return Response(data= {'message':'Invalid credentials'})
            
            

    def get(self,request):
        content= {'user': str(request.user), 'auth':str(request.auth)}
        return Response(data= content, status= status.HTTP_200_OK)
        






































# class SignupView(generics.GenericAPIView, mixins.ListModelMixin):
#     serializer_class= Signupserializer 
#     queryset= User.objects.all() 
    
#     def get(self, request:Request):     
#         return self.list(request)
     
 
#     def post(self, request:Request):
#         serializer= self.serializer_class(data= request.data)        
#         if serializer.is_valid():
#             serializer.save()            
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
                
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

    
        
        
            
        
            
    

