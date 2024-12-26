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
    
    # Fetch the current logged-in user
    user = request.user
    
    # Get the associated profile using the related_name 'profile' from the User model
    user_profile = user.profile
    
    # Optionally, you can also fetch the user's recipes if needed
    recipes = user.recipes.all()
    
    # Return the context to the template
    return render(request, 'accounts/userprofile.html', {
        'user': user,
        'user_profile': user_profile,
        'recipes': recipes
    })