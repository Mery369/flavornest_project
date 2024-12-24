from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signin/', views.signin, name="signin"),  
]
