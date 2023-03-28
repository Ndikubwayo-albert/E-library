from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter




router= DefaultRouter()
router.register('users', views.UserViewset, basename='users')

urlpatterns = [ 
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='createaccount'),
    
    # for API authentication
    
    path('register-api/', include(router.urls)),
    
    # path('Register/', include(router.urls)),
    # path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair")
    
    # path('createuser/', views.SignupView.as_view(), name='createuser'),
    # path('login/', views.LoginView.as_view(), name='login'),
    
    
]