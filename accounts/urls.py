from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name="signin"),  
    path('signup/', views.signup, name="signup"),
    path('profile/', views.user_profile, name='profile'),
    
]
