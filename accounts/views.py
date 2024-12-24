from django.shortcuts import render , redirect
from django.contrib import auth
from django.contrib.auth.models import User
from accounts.models import UserProfile 
from blog.models import Recipe
# Create your views here.

def signin(request):

    return render(request, 'accounts/signin.html', {'title': 'Sign In'})

def signup(request):

    if request.method == "POST":
     first_name = request.POST['firstname']
     last_name = request.POST['lastname']
     email = POST['email']
     password = POST['password']
     confirm_password = POST['confirmpassword']
     profile_image = POST['profilepic']
     bio = POST['bio']
     location = POST['location']
     if password == confirm_password :
        if User.objects.filter(email=email).exists():
            return redirect('accounts:signup')
        else :
            new_user =UserProfile.objects.create_user(first_name=first_name, last_name=last_name ,
            email = email , password = password , profile_image = profile_image , bio = bio ,
            location = location)
            new_user.save()
            user_credentials = auth.authenticate(email=email , password = password)
            auth.login(request , user_credentials)
            return redirect ('accounts:userprofile')
     else :
        return redirect('accounts:signup')
    return render(request, 'accounts/signup.html', {'title': 'Register'})

def user_profile(request):
    # Fetch the user's profile and their recipes
    user_profile = request.user.profile
    recipes = Recipe.objects.filter(author=request.user)
    
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'recipes': recipes,
    })