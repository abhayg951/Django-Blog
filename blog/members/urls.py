from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register", views.CreateUserView.as_view(), name="register")
]
