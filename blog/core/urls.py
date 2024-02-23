from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("blog/<int:pk>", views.BlogDetailView.as_view(), name="blog-detail"),
    path("blog-add", views.CreateBlogView.as_view(), name='blog-add'),
    path("blog/edit/<int:pk>",views.UpdateBlogView.as_view(), name="blog-edit"),
    path("blog/delete/<int:pk>", views.DeleteBlogView.as_view(), name='blog-delete'),
    path("add-category", views.CreateCategoryView.as_view(), name="create-category"),
    path("category/<str:cats>", views.CategoryView, name="get-category"),
    path("category-list", views.CategoryListView, name="category-list")
]