from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import UserProfile 
from blog.models import Recipe
from django.contrib import messages

# Create your views here.

def signin(request):

    
      if request.user.is_authenticated:
        return redirect('accounts:profile')

      if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request , 'Login successful. Welcome back!')
                return redirect('accounts:profile') 

            else:
                # Invalid credentials - show an error message
                messages.error(request, 'Invalid username or password')
                return redirect('accounts:signin')  # Stay on the sign-in page if login fails
        else:
            # If form is invalid, show an error message
            messages.error(request, 'Invalid form submission')
            return redirect('accounts:signin')  # Stay on the sign-in page if form is invalid
      else:
        form = AuthenticationForm()

      return render(request, 'accounts/signin.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        location = request.POST['location']
        bio = request.POST['bio']
        profile_picture = request.FILES.get('profilepic')  # Use request.FILES for handling file uploads
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']

        # Ensure the passwords match
        if password == confirm_password:
            # Check if the email or username already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already taken.")
                return redirect('accounts:signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken.")
                return redirect('accounts:signup')
            else:
                # Create the user instance
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)

                # Create the associated user profile
                user_profile = UserProfile.objects.create(
                    user=user, 
                    first_name=first_name, 
                    last_name=last_name,
                    location=location,
                    bio=bio,
                    profile_image=profile_picture  # Ensure the profile picture is saved
                )
                
                # Log the user in after successful creation
                login(request, user)

                messages.success(request, "Account successfully created! Welcome to our community")
                return redirect('accounts:profile') 

        else:
            messages.error(request, "Passwords do not match.")
            return redirect('accounts:signup')

    return render(request, 'accounts/signup.html')


# def signout(request):
    
#         auth.logout(request)
#         messages.success(request, "You have been successfully logged out.")
#         return redirect('home')  
    

        
@login_required
def user_profile(request):
    
    user = request.user

    try:
        # Get the associated profile using the related_name 'profile' from the User model
        user_profile = user.profile
    except UserProfile.DoesNotExist:
        # Handle the case where the user is not registered
        messages.error(request, "You don't have a profile. Please complete your profile setup.")
        return redirect('accounts:signup')  

    #  fetch the user's recipes if needed
    recipes = user.recipes.all()

    return render(request, 'accounts/userprofile.html', {
        'user': user,
        'user_profile': user_profile,
        'recipes': recipes
    })