from django.urls import path
from .views import BlogDetailView, HomeView, CreateBlogView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blog/<int:pk>", BlogDetailView.as_view(), name="blog-detail"),
    path("blog-add", CreateBlogView.as_view(), name='blog-add')
]