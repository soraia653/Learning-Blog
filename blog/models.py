from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from taggit.models import TagBase, ItemBase
from taggit.managers import TaggableManager

from treebeard.mp_tree import MP_Node

class Tag(TagBase, MP_Node):

    node_order_by = ['name']

class TaggedPost(ItemBase):
    content_object = models.ForeignKey('Post', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', related_name="tagged_posts", on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('content_object', 'tag')

    def __str__(self):
        return self.tag.name

class Post(ItemBase):
    title = models.CharField(max_length=125, unique=True)
    slug_title = models.SlugField(max_length=255, unique=True)
    summary = models.TextField(max_length=100)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    tags = TaggableManager(through='TaggedPost', blank=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug_title = slugify(self.title)
        super(Post, self).save(*args, **kwargs)