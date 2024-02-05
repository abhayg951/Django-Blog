from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import BlogPostForm, UpdateBlogPostForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    model = models.BlogPost
    template_name = 'index.html'
    ordering = ["-created_at"]

class BlogDetailView(DetailView):
    model = models.BlogPost
    template_name = 'blog_details.html'

class CreateBlogView(CreateView):
    model = models.BlogPost
    template_name = 'add_blog.html'
    form_class = BlogPostForm
    # fields = "__all__"
    # fields = ('title', 'body')

class UpdateBlogView(UpdateView):
    model = models.BlogPost
    template_name = 'update_blog.html'
    form_class = UpdateBlogPostForm

class DeleteBlogView(DeleteView):
    model = models.BlogPost
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')