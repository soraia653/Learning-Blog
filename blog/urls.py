from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name="main_page"),
    path('drafts', views.DraftPostView.as_view(), name="drafts"),
    path('login', views.CustomLoginView.as_view(), name="login"),
    path('logout', views.CustomLogoutView.as_view(), name="logout"),
    path('read_post/<int:post_id>', views.read_post, name="read_post"),
    path('new_post', views.NewPostView.as_view(), name="new_post"),
    path('edit_post/<int:pk>', views.EditPostView.as_view(), name="edit_post"),
    path('delete_post/<int:pk>', views.DeletePostView.as_view(), name="delete_post"),
    path('tags/posts/<int:tag_id>', views.get_posts_per_tag, name="posts_per_tag"),
    path('registration', views.register_view, name="registration"),
]