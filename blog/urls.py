from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    
]