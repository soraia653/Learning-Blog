from typing import Any
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, User
from .forms import PostForm, CommentForm

# Create utility functions here.
def generate_tags_dict():

    all_tags = Post.tags.all().order_by('name')
    tags_dict = {}

    for tag in all_tags:
        first_letter = tag.name[0].upper()
        if first_letter not in tags_dict:
            tags_dict[first_letter] = {'tags': [], 'count': 0}
        tags_dict[first_letter]['tags'].append(tag)
        tags_dict[first_letter]['count'] += 1

    sorted_keys = sorted(tags_dict.keys())
    return sorted_keys, tags_dict

# Create function-based views here.
def register_view(request):

    if request.method == "POST":
        username = request.POST.get("username")

        # make sure email is a valid email
        email = request.POST.get("email")

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e)
            return render(request, "blog/registration.html")

        # ensure password and confirmation match
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")

        if password != confirmation:
            messages.error(request, "Passwords do not match.")
            return render(request, "blog/registration.html")
        
        # create new user
        try:
            new_user = User.objects.create_user(username, email, password)
            new_user.save()
            login(request, new_user)
            return redirect("main_page")
        except IntegrityError as e:
            messages.error(request, f"Something went wrong: {e}")
            return render(request, "blog/registration.html")
    
    return render(request, "blog/registration.html")

def index(request):
    all_posts = Post.objects.filter(status="published")

    sorted_keys, tags_dict = generate_tags_dict()

    context_dict = {
        "posts": all_posts,
        "sorted_keys": sorted_keys,
        "tags_dict": tags_dict,
    }

    return render(request, "blog/all_posts.html", context_dict)

def read_post(request, post_id):
    select_post = Post.objects.get(id=post_id)

    sorted_keys, tags_dict = generate_tags_dict()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = select_post
            comment.username = request.user
            comment.save()
            return redirect('read_post', post_id)
    else:
        form = CommentForm()

    context_dict = {
        "post": select_post,
        "sorted_keys": sorted_keys,
        "tags_dict": tags_dict,
        "form": form
    }

    return render(request, "blog/read_post.html", context_dict)

def get_posts_per_tag(request, tag_id):

    filtered_posts = []
    
    if request.method == "POST":
        filtered_posts = Post.objects.filter(tags__id=tag_id)
    
    all_tags = Post.tags.all().order_by('name')

    # create dictionary for tags from A-Z
    tags_dict = {}

    for tag in all_tags:
        first_letter = tag.name[0].upper()
        if first_letter not in tags_dict:
            tags_dict[first_letter] = {'tags': [], 'count': 0}
        tags_dict[first_letter]['tags'].append(tag)
        tags_dict[first_letter]['count'] += 1
    
    sorted_keys = sorted(tags_dict.keys())

    context_dict = {
        "filtered_posts": filtered_posts,
        "sorted_keys": sorted_keys,
        "tags_dict": tags_dict,
    }

    return render(request, "blog/posts_per_tag.html", context_dict)

# Create class-based views here.
class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/new_post.html"
    success_url = reverse_lazy("main_page")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/edit_post.html"
    success_url = reverse_lazy("main_page")


class DraftPostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/all_drafts.html"
    context_object_name = "drafts"

    def get_queryset(self):
        author = self.request.user
        return Post.objects.filter(author=author, status='draft')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        sorted_keys, tags_dict = generate_tags_dict()
        context['sorted_keys'] = sorted_keys
        context['tags_dict'] = tags_dict

        return context

class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy("main_page")

class CustomLoginView(LoginView):
    template_name = "blog/all_posts.html"
    next_page = reverse_lazy("main_page")

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("main_page")
