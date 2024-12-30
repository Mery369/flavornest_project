from .models import Comment,Rating,Recipe
from django import forms
 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

    def __init__(self, *args, **kwargs):
        super(RatingForm, self).__init__(*args, **kwargs)
        self.fields['rating'].widget = forms.RadioSelect(choices=[(i, '★') for i in range(1, 6)])
        # self.fields['rating'].widget.attrs.update({'class': 'rating-stars'})  # Optional for styling

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'slug', 'ingredients', 'instructions', 'prep_time', 'cook_time', 'recipe_image', 'category']

    # Customizing the form fields (optional)
    # def __init__(self, *args, **kwargs):
    #     super(RecipeForm, self).__init__(*args, **kwargs)
    #     self.fields['recipe_name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['slug'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['ingredients'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['instructions'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['prep_time'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['cook_time'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['recipe_image'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['category'].widget.attrs.update({'class': 'form-control'})