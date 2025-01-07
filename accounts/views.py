from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import UserProfile 
from blog.models import Recipe,Rating
from django.contrib import messages
from .forms import CollaborateForm, EditProfileForm

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


def signout(request):
    
    logout(request)  
    messages.success(request, "You have been successfully logged out.")  
    return redirect('blog:home')  
    

        
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

    #  fetch the user's recipes 
    recipes = user.recipes.all()
    #  fetch the user's reviews
    reviews = Rating.objects.filter(user=user)
      # Fetching all other registered users for the friend suggestion
    suggested_users = User.objects.exclude(id=user.id)  # Exclude the logged-in user

    # Ensure fetching UserProfile objects along with User
    suggested_users_with_profile = UserProfile.objects.filter(user__in=suggested_users)

    return render(request, 'accounts/userprofile.html', {
        'user': user,
        'user_profile': user_profile,
        'recipes': recipes,
        'reviews': reviews,
        'suggested_users': suggested_users_with_profile,
    })

def collab_form(request):
    
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS,
             "Collaboration request Sent Successfully!")

    else:
        # For GET request, initialize an empty form
        collaborate_form = CollaborateForm()

    return render(
        request,
        "accounts/collaborate_form.html",
        {
            
            "collaborate_form": collaborate_form
        },
    )

# Edit profile View
@login_required
def edit_profile(request):
    user_profile = request.user.profile  # Assuming you have a related UserProfile model

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('accounts:profile')  # Redirect to profile page after success
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EditProfileForm(instance=user_profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

# Delete account view
@login_required
def delete_profile(request):
    user = request.user.profile
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('accounts:signup')  # Redirect to signup page after deletion
    return render(request, 'accounts/delete_profile.html')  # Show a confirmation page