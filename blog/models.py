from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class UserProfile(models.Model):
    """
    Represents a user profile that extends the built-in Django User model.
    This model contains additional fields like profile image, bio, location, and name.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_image = CloudinaryField('image', default='placeholder')
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the UserProfile instance.
        Typically used to display the profile in the admin panel.
        
        Returns:
            str: The username of the associated user, followed by the word 'Profile'.
        """
        return f"{self.user.first_name} {self.last_name}'s Profile"


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
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating should be between 1 and 5"
    )
      

    class Meta:
        # Ensure a user can only rate a recipe once
        unique_together = ['recipe', 'user']


    def __str__(self):
        """
        Returns a string representation of the rating, showing user and rating value.
        """
        return f"Rating for {self.recipe.name} by {self.user.first_name} - {self.rating} stars"



class Comment(models.Model):
    """
    Represents a comment left by a user on a recipe.
    Each comment is linked to a specific recipe and a user.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name = "comments")  
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="commenter"
    )
    comment_text = models.TextField()  
    date_added = models.DateTimeField(auto_now_add=True)  
    approved = models.BooleanField(default= False)

    class Meta:
        ordering = ["date_added"]

    def __str__(self):
        """
        Returns a string representation of the comment, including user and recipe name.
        """
        return f"Comment by User {self.user_id} on {self.recipe.name}"
