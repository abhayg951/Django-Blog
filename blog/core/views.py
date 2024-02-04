from django.views.generic import ListView, DetailView, CreateView
from . import models

# Create your views here.

class HomeView(ListView):
    model = models.BlogPost
    template_name = 'index.html'

class BlogDetailView(DetailView):
    model = models.BlogPost
    template_name = 'blog_details.html'

class CreateBlogView(CreateView):
    model = models.BlogPost
    template_name = 'add_blog.html'
    fields = '__all__'