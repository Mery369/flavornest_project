from django.shortcuts import render



def page_diet(request):
    return render(request, 'pages/about_diet.html')