from django.urls import path
from .views import BlogDetailView, HomeView, CreateBlogView, UpdateBlogView, DeleteBlogView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blog/<int:pk>", BlogDetailView.as_view(), name="blog-detail"),
    path("blog-add", CreateBlogView.as_view(), name='blog-add'),
    path("blog/edit/<int:pk>", UpdateBlogView.as_view(), name="blog-edit"),
    path("blog/delete/<int:pk>", DeleteBlogView.as_view(), name='blog-delete')
]