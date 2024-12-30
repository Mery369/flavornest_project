from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Avg
from django.views import generic
from django.contrib import messages
from .models import Recipe,Category
from .forms import CommentForm

# Create your views here.


class RecipeList(generic.ListView):
    queryset = Recipe.objects.all().order_by('-created_on')[:6]  # Get the 6 latest recipes, ordered by 'created_on'
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
    recipes = Recipe.objects.all().order_by('-created_on')[:6]
    categories = Category.objects.all()
    return render(request, 'blog/recipe_list.html', {'recipes': recipes,'categories': categories, })


def category_recipes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.recipe_set.all()  # This assumes a ForeignKey from Recipe to Category
    return render(request, 'blog/category_recipes.html', {
        'category': category,
        'recipes': recipes,
    })

def home(request):
    search_query = request.GET.get('q', '')  # Get the search query for recipes

    # Get all categories (optional, if you want to show category names in the search results)
    categories = Category.objects.all()

    # Filter recipes based on the search query, including category names
    recipes = Recipe.objects.all()

    if search_query:
        # First, try searching for recipe names
        recipes = recipes.filter(recipe_name__icontains=search_query)
        
        # Then, try searching for category names (if the query matches any category name)
        categories = categories.filter(name__icontains=search_query)
        
        # If a matching category is found, filter recipes by that category
        if categories.exists():
            category_ids = categories.values_list('id', flat=True)
            recipes = recipes.filter(category__id__in=category_ids)

    # Pagination (optional)
    recipes = recipes.order_by('-created_on')  # You can also order them based on creation date, if you prefer

    # Pagination setup
    is_paginated = recipes.paginator.num_pages > 1
    page_obj = recipes

    return render(request, 'home.html', {
        'recipes': recipes,
        'categories': categories,
        'is_paginated': is_paginated,
        'page_obj': page_obj,
        'search_query': search_query,
    })