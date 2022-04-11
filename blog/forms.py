from .models import Comment, Post, Category
from django import forms

choices = Category.objects.all().values_list('name', 'name')
choice_list = [choice for choice in choices]


class CommentForm(forms.ModelForm):
    """
    
    """

    class Meta:
        """
        
        """

        model = Comment
        fields = ('body',)
        labels = {'body': ''}


class AddPostForm(forms.ModelForm):
    """
    
    """

    class Meta:
        """
        
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
    
    """

    class Meta(AddPostForm.Meta):
        """
        
        """

        exclude = ('featured_image',)
