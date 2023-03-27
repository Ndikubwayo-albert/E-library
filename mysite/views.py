from django.shortcuts import redirect, render
from django.conf import settings

from django.http import HttpResponse
from django.contrib import messages

from .forms import Bookform
from .models import Book

from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import ListView

# from django.contrib.auth.forms import UserCreationForm
from .serializers import Book_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



# Create your views here.

def homepage(request):    
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'about.html') 

def books(request):
    all= Book.objects.all()
    context={
    'books' :all     
    }
    
    return render(request, 'books.html', context) 


def register_book(request):
    if request.method == 'POST':
        
        form= Bookform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Book added successfully !')                
            return redirect('/register_book')
  
    context= {
        'form': Bookform
        }
         
    return render(request, 'add_book.html', context)


def contact(request):
    if request.method == 'GET':
        form = Contactform()
    else:
        form= Contactform(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
                        
            message = message + "\nFrom: " + from_email + "]nPhone:" + phone
            
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                messages.error(request, 'Failed to send Email!')
                return HttpResponse('Invalid header found.')
            
            messages.success(request, ('Thanks '+ name +', your message has been received.'))
            
            form = Contactform()            
    return render(request, "contact.html", {'form': form})


	
class records_control(ListView):
    model = Book
    template_name = 'records_manager.html'
    context_object_name = 'allbooks'
                                                                                                                                                                                                   

def book_delete(request, pk):
    book= Book.objects.get(id=pk)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('/books_control')

# Views related to API 

# @api_view(['GET','POST'])
# def books_list(request):
#     if request.method== 'GET':
#         allbooks= Book.objects.all()
#         serializer= Book_serializer(allbooks, many= True)
#         return Response(serializer.data)
#     if request.method== 'POST':
#         serializer= Book_serializer(data= request.data)
#         if serializer.is_valid():                
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

# @api_view(['GET','PUT','DELETE'])    
# def book_details(request, pk):
#     try:
#         book= Book.objects.get(pk= pk)
#     except Book.DoesNotExist:
#         return HttpResponse(status= status.HTTP_404_NOT_FOUND)
    
#     if request.method=='GET':
#         serializer= Book_serializer(book) 
#         return Response(serializer.data)
    
#     elif request.method=='PUT':
#         serializer= Book_serializer(book, data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#     elif request.method=='DELETE':
#         book.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
    
    
# class BookDetails(APIView):
#     def get_object(self, id):
#         try:
#             return Book.objects.get(id= id)
#         except Book.DoesNotExist:
#             return HttpResponse(status= status.HTTP_404_NOT_FOUND)           
                
#     def get(self,request, id):
#         book= self.get_object(id)
#         serializer= Book_serializer(book)
#         return Response(serializer.data)
        
#     def put(self, request, id):
#         book= self.get_object(id)
#         serializer= Book_serializer(book, data= request.data)
#         if serializer.is_valid():                
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         book= self.get_object(id)
#         book.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
                   
    
    
class BooksAPIView(APIView):
    def get(self, request):
        allbooks= Book.objects.all()
        serializer= Book_serializer(allbooks, many= True) 
        return Response(serializer.data)
        
    def post(self, request):
        serializer= Book_serializer( data= request.data)
        if serializer.is_valid():                
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
        

class Book_details(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class= Book_serializer
    queryset= Book.objects.all() 
       
    lookup_field= 'id'
    permission_classes= [IsAuthenticated]
    authentication_classes= [TokenAuthentication]
        
    def get(self, request, id= None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
        
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id= None):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)
    
    
class BookViewSet(viewsets.ViewSet):
        
    permission_classes= [IsAuthenticated]
    
    def list(self, request):
        allbooks= Book.objects.all()
        serializer= Book_serializer(allbooks, many= True)            
        return Response(serializer.data)
    
    def create(self, request):
        serializer= Book_serializer(data= request.data)
        if serializer.is_valid():                
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST) 
    
    def retrieve(self, request, pk= None):
        allbooks= Book.objects.all()
        book= get_object_or_404(allbooks, pk= pk)
        serializer= Book_serializer(book)
        return Response(serializer.data) 
     
    def update(self, request, pk=None):
        book= Book.objects.get(pk= pk)
        serializer= Book_serializer(book,data= request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book= Book.objects.get(pk= pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
# def get_version(self):
#     if self.request=='v1':
#         return Book_serializer
#     else:
#         return Book_serializerV2      
