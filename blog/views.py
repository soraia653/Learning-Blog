from django.shortcuts import render
from .models import Post

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