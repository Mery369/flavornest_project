from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Avg
from django.views import generic
from .models import Recipe
# Create your views here.

# def recipe_detail(request, recipe_id):
#     recipe = get_object_or_404(Recipe, id=recipe_id)
    
#     # Get all ratings for the recipe
#     ratings = recipe.ratings.all()
    
#     # Calculate average rating
#     average_rating = ratings.aggregate(Avg('rating'))['rating__avg']
    
#     return render(request, 'recipe_detail.html', {
#         'recipe': recipe,
#         'ratings': ratings,
#         'average_rating': average_rating,
#     })
class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = 'blog/home.html'  
    context_object_name = 'recipes'  

def recipe_detail(request, slug):
    """
    Display an individual :model:`blog.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`blog.Recipe`.

    **Template:**

    :template:`blog/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/recipe_detail.html",
        {"recipe": recipe},
    )