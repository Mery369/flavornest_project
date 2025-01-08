from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Avg
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .models import Recipe,Category,Rating
from .forms import RatingForm,RecipeForm, SearchForm

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
    `rating_form``
        An instance of :rating_form:`RatingForm`.
    **Template:**

    :template:`blog/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    
    reviews = recipe.ratings.all().order_by("-created_at")
    rating_count = recipe.ratings.count()
    # Calculate the average rating of the recipe
    avg_rating = recipe.ratings.aggregate(Avg('rating'))['rating__avg'] or 0
    stars = range(1, 6)
    user_rating = None
    rating_form = None

    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
        
        if request.method == "POST":
            if user_rating:
                messages.info(request, "You've already rated this recipe. You can't submit another review.")
            else:
                rating_form = RatingForm(data=request.POST)
                if rating_form.is_valid():
                    rating = rating_form.save(commit=False)
                    rating.recipe = recipe
                    rating.user = request.user
                    rating.save()
                    messages.success(request, 'Your rating has been submitted successfully!')
            return redirect('blog:recipe_detail', slug=slug)
        else:
            rating_form = RatingForm() if not user_rating else None

    return render(
        request,
        "blog/recipe_detail.html",
        {
            "recipe": recipe,
            'title': 'Recipe Details',
            'avg_rating': avg_rating,
            "stars": stars,
            "reviews": reviews,
            "rating_form": rating_form,
            "user_rating": user_rating,
            "rating_count": rating_count,
        },
    )

def recipe_list(request):
    # Fetching all recipes, ordered by creation date (most recent first)
    recipes = Recipe.objects.filter(status=1).order_by('-created_on')
    categories = Category.objects.all()
     # Set the number of recipes per page
    paginator = Paginator(recipes, 8) 

    # Get the page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)
    # Check if there's a search query in the GET request
    query = request.GET.get('query', '')

    if query:
        recipes = recipes.filter(recipe_name__icontains=query) 
    return render(request, 'blog/recipe_list.html', {'recipes': recipes,'categories': categories, 'page_obj': page_obj,'query': query,})


def category_recipes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.recipe_set.filter(status=1).order_by('-created_on')
    return render(request, 'blog/category_recipes.html', {
        'category': category,
        'recipes': recipes,
    })


def rate_recipe(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)

    # Check if the user is logged in
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to rate this recipe.")
        return redirect('login') 

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


