from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("home")
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})