from django.urls import path, include, re_path as url
from . import views
# from django.contrib.auth import views as auth_views
# from users import views as user_views
from rest_framework.routers import DefaultRouter



router= DefaultRouter()
router.register('books', views.BookViewSet, basename='books')


urlpatterns = [    
    
    path('', views.homepage, name='homepage'),    
    path('home/', views.homepage, name='homepage'),    
    path('about/', views.aboutus),
    path('contact/', views.contact),
    
    path('books/',views.books, name='book'),
    path('books_control/', views.records_control.as_view(), name='allbooks'),
    path('books/delete/<str:pk>/',views.book_delete, name='bookdelete'),
    # path('books/',views.books, name='book'),    
    # path('signin/',auth_views.LoginView.as_view(template_name='signin.html'), name='signin'),
   
    path('register_book/',views.register_book, name='registerbook'),

    
    # for rest_framework
    
    #path('books_list/', views.books_list),
    # path('detail/<int:pk>/', views.book_details),
    # path('book_details/<int:id>/', views.BookDetails.as_view()),
    
    path('booksapi/', views.BooksAPIView.as_view()),  
    path('book_details/<int:id>/', views.Book_details.as_view()), 
    
    path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>/', include(router.urls)),
    
      
 
   
]