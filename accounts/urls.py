from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
   
    path('collab/', views.collab_form , name ="collaborate_form"),
    path('signin/', views.signin, name="signin"),  
    path('logout/', views.custom_logout, name='account_logout'),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.user_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    
]
