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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
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

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"