from django.urls import path
from .views import index, read_post

urlpatterns = [
    path('', index, name="main_page"),
    path('read_post/<int:post_id>', read_post, name="read_post"),
]