from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=125, unique=True)
    slug_title = models.SlugField(max_length=255, unique=True)
    summary = models.TextField(max_length=200)
    image_url = models.URLField(blank=True)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    tags = TaggableManager()

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug_title = slugify(self.title)
        super(Post, self).save(*args, **kwargs)