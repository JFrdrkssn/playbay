from .models import Comment, Post, Category
from django import forms

# Loop through category names added on admin page.
# Add them to choice list select when users adds/edits posts
choices = Category.objects.all().values_list('name', 'name')
choice_list = [choice for choice in choices]


class CommentForm(forms.ModelForm):
    """
    Form for commenting on posts.
    """

    class Meta:
        """
        Allowed fields.
        Remove label for body field.
        """

        model = Comment
        fields = ('body',)
        labels = {'body': ''}


class AddPostForm(forms.ModelForm):
    """
    Form for adding posts.
    """

    class Meta:
        """
        Allowed fields.
        Widgets for styling
        and placeholder text.
        """

        model = Post
        fields = ('category', 'title', 'excerpt', 'content', 'featured_image')

        widgets = {
            'category': forms.Select(choices=choice_list, attrs={
                'class': 'form-select',
                }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required'
                }),
            'excerpt': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required'
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Required'
                }),
            'featured_image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
                })
        }


class EditPostForm(AddPostForm):
    """
    Form for editing posts.
    Inherits from AddPostForm.
    """

    class Meta(AddPostForm.Meta):
        """
        Exclude image field when editing posts.
        Inherits from AddPostForm
        """

        exclude = ('featured_image',)
