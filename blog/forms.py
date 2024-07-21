from django import forms
from django.forms import TextInput, Textarea
from taggit.forms import TagWidget
from .models import Post, Comment

from django_ckeditor_5.widgets import CKEditor5Widget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "summary", "image_url", "body", "status", "tags"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Insert the title of your post.",
                    "class": "form-control",
                }
            ),
            "summary": forms.Textarea(
                attrs={
                    "placeholder": "Insert a quick description about your post.",
                    "class": "form-control",
                    "rows": "3",
                }
            ),
            "image_url": forms.URLInput(
                attrs={
                    "placeholder": "Enter image URL.",
                    "class": "form-control",
                }
            ),
            "body": CKEditor5Widget(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "tags": TagWidget(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)
        labels = {"comment": ""}
        widgets = {
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Leave your comment here.",
                    "rows": 4,
                }
            )
        }
