from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg

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