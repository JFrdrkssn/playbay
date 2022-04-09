from .models import Comment, Post
from django import forms


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
        fields = ('title', 'excerpt', 'content', 'featured_image')

        widgets = {
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
