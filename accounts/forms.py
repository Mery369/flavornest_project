from .models import CollaborateRequest
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from cloudinary.forms import CloudinaryFileField

class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')

class EditProfileForm(forms.ModelForm):
    # Form fields to edit User model fields
    first_name = forms.CharField(max_length=100, required=True, label="First Name")
    last_name = forms.CharField(max_length=100, required=True, label="Last Name")
    email = forms.EmailField(required=True, label="Email Address")

    # Form fields to edit UserProfile model fields
    profile_image = CloudinaryFileField(required=False, label="Profile Image")
    bio = forms.CharField(widget=forms.Textarea, required=False, label="Bio")
    location = forms.CharField(max_length=100, required=False, label="Location")

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'profile_image', 'bio', 'location']

    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance').user
        super().__init__(*args, **kwargs)
        # Pre-populate User data in the form
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['email'].initial = user.email

    def save(self, commit=True):
        # Save the user part of the form
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        # Save the UserProfile part
        user_profile = self.instance
        user_profile.profile_image = self.cleaned_data['profile_image']
        user_profile.bio = self.cleaned_data['bio']
        user_profile.location = self.cleaned_data['location']
        if commit:
            user_profile.save()

        return user_profile