from . import views
from django.urls import path

app_name = 'pages'  # Updated the app_name

urlpatterns = [
    path('', views.page_diet, name='page_diet'),  
]