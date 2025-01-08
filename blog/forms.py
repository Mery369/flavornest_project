from .models import Rating, Recipe
from django import forms
 



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
    
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)