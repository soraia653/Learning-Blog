from django.urls import path
from .views import index, login_view, logout_view, register_view, read_post, new_post

urlpatterns = [
    path('', index, name="main_page"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('read_post/<int:post_id>', read_post, name="read_post"),
    path('new_post', new_post, name="new_post"),
    path('registration', register_view, name="registration"),
]