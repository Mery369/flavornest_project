from django.shortcuts import render

# Create your views here.

def signin(request):

    return render(request, 'accounts/signin.html', {'title': 'Sign In'})

def signup(request):

    return render(request, 'accounts/signup.html', {'title': 'Register'})