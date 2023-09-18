from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'published_date']

# Register your models here.
admin.site.register(Post, PostAdmin)