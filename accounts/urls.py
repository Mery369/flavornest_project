from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    
    path('signin/', views.signin, name="signin"),  
    path('signup/', views.signup, name="signup"),
    path('profile/', views.user_profile, name='user_profile'),
]
