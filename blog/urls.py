from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="main_page"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('read_post/<int:post_id>', read_post, name="read_post"),
    path('edit_post/<int:post_id>', edit_post, name="edit_post"),
    path('delete_post/<int:post_id>', delete_post, name="delete_post"),
    path('new_post', new_post, name="new_post"),
    path('registration', register_view, name="registration"),
]