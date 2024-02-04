from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length = 200, default="my_tag")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
    
    