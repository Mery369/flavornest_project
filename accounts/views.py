from django.shortcuts import render , redirect
from django.contrib import auth
from django.contrib.auth.models import User
from accounts.models import UserProfile 
from blog.models import Recipe
# Create your views here.

def signin(request):

    return render(request, 'accounts/signin.html', {'title': 'Sign In'})

def signup(request):

    return render(request, 'accounts/signup.html', {'title': 'Register'})
    

def user_profile(request):
    # Fetch the user's profile and their recipes
    user_profile = request.user.profile
    recipes = Recipe.objects.filter(author=request.user)
    
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'recipes': recipes,
    })