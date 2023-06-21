from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import Post, User
from .forms import PostForm

# Create your views here.
def index(request):
    all_posts = Post.objects.all()

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
        "posts": all_posts,
        "sorted_keys": sorted_keys,
        "tags_dict": tags_dict,
    }

    return render(request, "blog/all_posts.html", context_dict)

def read_post(request, post_id):
    select_post = Post.objects.get(id=post_id)

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
        "post": select_post,
        "sorted_keys": sorted_keys,
        "tags_dict": tags_dict,
    }

    return render(request, "blog/read_post.html", context_dict)

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = User.objects.get(username=request.user)
            new_post.save()
            form.save_m2m()
            return redirect("main_page")
    else:
        form = PostForm()

    context_dict = {
        "form": form,
    }

    return render(request, "blog/new_post.html", context_dict)

def edit_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect("main_page")
    else:
        form = PostForm(instance=post)
    
    context_dict = {
        "form": form,
        "post": post,
    }

    return render(request, "blog/edit_post.html", context_dict)

def delete_post(request, post_id):
    
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect("main_page")
    
    context_dict = {
        "post": post,
    }
    
    return render(request, "blog/delete_post.html", context_dict)


    return render(request)

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

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect("main_page")
        else:
            error_dict = {
                "message": "Invalid username and/or password."
            }

            return render(request, "blog/all_posts.html", error_dict)
    
    return redirect("main_page")

def logout_view(request):
    logout(request)
    return redirect("main_page")

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