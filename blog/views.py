from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Avg
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm

# Create your views here.


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
    comments = recipe.comments.all().order_by("-date_added")
    comment_count = recipe.comments.filter(approved=True).count()
    if request.method == "POST":
       comment_form = CommentForm(data=request.POST)
       if comment_form.is_valid():
           comment = comment_form.save(commit=False)
           comment.author = request.user
           comment.recipe = recipe
           comment.save()
           messages.add_message(
           request, messages.SUCCESS,
           'Comment submitted and awaiting approval'
                                 )

    comment_form = CommentForm()

    return render(
        request,
        "blog/recipe_detail.html",
        {"recipe": recipe,
        'title' :'Recipe Details',
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
         
    )


def recipe_list(request):
    # Fetching all recipes, ordered by creation date (most recent first)
    recipes = Recipe.objects.all().order_by('-created_on')  
    return render(request, 'blog/recipe_list.html', {'recipes': recipes})


def home(request):
    search_query = request.GET.get('q', '')

    # If there is a search query, filter recipes based on the query
    if search_query:
        recipes = Recipe.objects.filter(recipe_name__icontains=search_query)
    else:
        recipes = Recipe.objects.all()

    # Pagination logic
    paginator = Paginator(recipes, 6)  # Show 6 recipes per page
    page_number = request.GET.get('page')  # Get the page number from the query params
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'recipes': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    })