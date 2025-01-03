from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Avg
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .models import Recipe,Category,Rating
from .forms import CommentForm,RatingForm,RecipeForm

# Create your views here.


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')[:6]  # Get the 6 latest recipes, ordered by 'created_on'
    template_name = 'blog/home.html'  
    context_object_name = 'recipes'  

def recipe_detail(request, slug):
    """
    Display an individual :model:`blog.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`blog.Recipe`.
    `comment_form``
        An instance of :forms:`CommentForm`.
    `rating_form``
        An instance of :rating_form:`RatingForm`.
    **Template:**

    :template:`blog/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-date_added")
    comment_count = recipe.comments.filter(approved=True).count()
    # Calculate the average rating of the recipe
    avg_rating = recipe.ratings.aggregate(Avg('rating'))['rating__avg']
    stars = range(1, 6)

    if request.method == "POST":
       comment_form = CommentForm(data=request.POST)
       rating_form = RatingForm(request.POST)
       if comment_form.is_valid():
           comment = comment_form.save(commit=False)
           comment.author = request.user
           comment.recipe = recipe
           comment.save()
           messages.add_message(
           request, messages.SUCCESS,
           'Comment submitted and awaiting approval')
         # Handling rating form submission
       if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.recipe = recipe
            rating.user = request.user
            rating.save()
            messages.success(request, 'Your rating has been submitted successfully!')
            return redirect('recipe_detail', slug=slug)

    # Initialize the forms
    comment_form = CommentForm()
    rating_form = RatingForm()
                            

  
    
    return render(
        request,
        "blog/recipe_detail.html",
        {"recipe": recipe,
        'title' :'Recipe Details',
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
         'avg_rating': avg_rating,
        "stars": stars,
        "rating_form": rating_form,
        },
         
    )


def recipe_list(request):
    # Fetching all recipes, ordered by creation date (most recent first)
    recipes = Recipe.objects.filter(status=1).order_by('-created_on')
    categories = Category.objects.all()
    return render(request, 'blog/recipe_list.html', {'recipes': recipes,'categories': categories, })


def category_recipes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.recipe_set.filter(status=1).order_by('-created_on')
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

def rate_recipe(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)

    # Check if the user is logged in
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to rate this recipe.")
        return redirect('login')  # Redirect to the login page or any other page you'd like

    # If the user has already rated this recipe, retrieve their existing rating
    existing_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            # If a rating already exists, update it; otherwise, create a new one
            if existing_rating:
                existing_rating.rating = form.cleaned_data['rating']
                existing_rating.save()
                messages.success(request, "Your rating has been updated.")
            else:
                Rating.objects.create(
                    recipe=recipe,
                    user=request.user,
                    rating=form.cleaned_data['rating']
                )
                messages.success(request, "Your rating has been submitted.")
            return redirect('recipe_detail', recipe_slug=recipe.slug)
    else:
        form = RatingForm(instance=existing_rating)

    return render(request, 'recipes/rate_recipe.html', {'form': form, 'recipe': recipe})

@login_required
def add_recipe(request):
    """
    Handles the creation of a new recipe.
    If the recipe is successfully created, it is awaiting approval.
    """
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form without committing to the database
            recipe = form.save(commit=False)
            # Automatically generate the slug from the recipe name
            recipe.slug = slugify(recipe.recipe_name)
            # Associate the recipe with the logged-in user
            recipe.author = request.user
            # Set the recipe's status to draft (awaiting approval)
            recipe.status = 0  # "Draft"
            recipe.save()

            # Show a success message
            messages.success(request, "Recipe successfully added and is awaiting approval.")
            # , slug=recipe.slug
            return redirect('accounts:profile')
    else:
        form = RecipeForm()

    return render(request, 'blog/add_recipe.html', {'form': form})

@login_required
def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, author=request.user)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe updated successfully!")
            return redirect('blog:recipe_detail', slug=recipe.slug)
        else:
            messages.error(request, "There was an error updating your recipe. Please try again.")
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'blog/edit_recipe.html', {'form': form, 'recipe': recipe})


@login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, author=request.user)
    
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect('accounts:profile')  
    
    return render(request, 'blog/delete_recipe_confirmation.html', {'recipe': recipe})

