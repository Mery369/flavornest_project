from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('category/<int:category_id>/', views.category_recipes, name='category_recipes'), 
    path('recipe/edit/<slug:slug>/', views.edit_recipe, name='edit_recipe'),
    path('recipe/delete/<slug:slug>/', views.delete_recipe, name='delete_recipe'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    
]