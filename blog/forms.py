from django import forms
from django.forms import TextInput, Textarea
from taggit.forms import TagWidget
from .models import Post

from ckeditor.fields import RichTextFormField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'summary', 'image_url', 'body', 'status', 'tags']
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
            'body': RichTextFormField(config_name='default'),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'tags': TagWidget(
                attrs={
                    'class' : 'form-control'
                }
            ),
        }
