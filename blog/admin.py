from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'published_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'post', 'create_date']

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)