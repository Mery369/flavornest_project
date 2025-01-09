from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    """
    Represents a category of recipes (e.g., Vegetarian, Vegan, Gluten-Free).
    Each recipe belongs to one category.
    """
    name = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

STATUS = ((0, "Draft"), (1, "Published"))
class Recipe(models.Model):
    """
    Represents a recipe, including its name, ingredients, 
    cooking instructions, and time details.
    Each recipe is assigned to one category.
    """
    recipe_name = models.CharField(max_length=200, unique=True) 
    slug = models.SlugField(max_length=200, unique=True)
    ingredients = models.TextField()  
    instructions = models.TextField()  
    prep_time = models.IntegerField()  
    cook_time = models.IntegerField()  
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    recipe_image = CloudinaryField('image', default='placeholder')
    approved = models.BooleanField(default=False) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="recipes"
    )
    status = models.IntegerField(choices=STATUS, default=0) 

    class Meta:
        ordering = ["-created_on"]

    @property
    def total_time(self):
        """
        Returns the total time required to prepare and cook the recipe 
        (prep_time + cook_time).
        """
        return self.prep_time + self.cook_time

    def __str__(self):
        """
        Returns the name of the recipe.
        """
        return self.recipe_name
    

class Rating(models.Model):
    """
    Represents a rating for a recipe. Users can rate a recipe and optionally leave a review.
    Each rating is linked to a specific recipe and a user.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ratings")  
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.IntegerField()
    review = models.TextField(max_length=500 , blank=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time the rating was created.")
    updated_at = models.DateTimeField(auto_now_add=True, null= True)

    class Meta:
        # Ensure a user can only rate a recipe once
        unique_together = ['recipe', 'user']


    def __str__(self):
        """
        Returns a string representation of the rating, showing user and rating value.
        """
        return f"Rating for {self.recipe.recipe_name} by {self.user.first_name} - {self.rating} stars : {self.updated_at}"





