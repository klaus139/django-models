from turtle import title
from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model

class post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    Text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

def get_absolute_url(self):
    return reverse('blog_post_detail', args=[self.slug])

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super(post, self).save(*args, **kwargs)

def __str__(self):
        return self.title
def get_user_model(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class Meta:
    ordering = ['created_date']

    def __unicode__(self):
            return self.title

...
class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

