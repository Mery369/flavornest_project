from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('category/<int:category_id>/', views.category_recipes, name='category_recipes'),  # for category-specific recipes
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    
]