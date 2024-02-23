from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import BlogPostForm, UpdateBlogPostForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    model = models.BlogPost
    template_name = 'index.html'
    ordering = ["-created_at"]

    def get_context_data(self, **kwargs):
        categories = models.Category.objects.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        context["cate_menu"] = categories
        return context
    

class BlogDetailView(DetailView):
    model = models.BlogPost
    template_name = 'blog_details.html'

    def get_context_data(self, **kwargs):
        categories = models.Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["cate_menu"] = categories
        return context

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


class CreateCategoryView(CreateView):
    model = models.Category
    template_name = 'add_category.html'
    fields = "__all__"

def CategoryView(request, cats):
    category_post = models.BlogPost.objects.filter(category=cats.replace("-", " "))
    return render(request, 'categories.html', {'cats':cats.replace("-", " "), 'category_post':category_post})

def CategoryListView(request):
    category_list = models.Category.objects.filter()
    return render(request, 'category_list.html', {'cate_list':category_list})