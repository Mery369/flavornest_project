from .models import Comment
from django import forms
from .models import Rating

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

    # Custom validator to make sure rating is between 1 and 5
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].widget = forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)])