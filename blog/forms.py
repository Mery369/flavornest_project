from .models import Comment,Rating,Recipe
from django import forms
 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating','review']

   

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name','ingredients', 'instructions', 'prep_time', 'cook_time', 'recipe_image', 'category']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 5, 'cols': 40}),  
            'instructions': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
    