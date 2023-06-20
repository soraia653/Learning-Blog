from django import forms
from django.forms import TextInput, Textarea
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'summary', 'image_url', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Insert the title of your post.', 
                    'class': 'form-control'
                    }
            ),
            'summary': forms.Textarea(
                attrs={
                    'placeholder': 'Insert a quick description about your post.',
                    'class': 'form-control',
                    'rows': '3'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Enter image URL.',
                    'class': 'form-control',
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'placeholder': 'Be creative!',
                    'class': 'form-control'
                }
            ),
            'tags': forms.TextInput(
                attrs={
                    'placeholder': 'Tag your post for easier search.', 
                    'class': 'form-control'
                    }
            ),
        }