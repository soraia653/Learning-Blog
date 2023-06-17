from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Post, User
from .forms import PostForm

# Create your views here.
def index(request):
    all_posts = Post.objects.all()

    context_dict = {
        "posts": all_posts,
    }

    return render(request, "blog/all_posts.html", context_dict)

def read_post(request, post_id):
    select_post = Post.objects.get(id=post_id)

    context_dict = {
        "post": select_post
    }

    return render(request, "blog/read_post.html", context_dict)

def new_post(request):
        
        if request.method == "POST":
            form = PostForm(request.POST)

            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.author = User.objects.get(username=request.user)
                new_post.save()
                return redirect("main_page")
        else:
            form = PostForm()

        context_dict = {
            "form": form,
        }

        return render(request, "blog/new_post.html", context_dict)

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