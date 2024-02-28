from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register", views.CreateUserView.as_view(), name="register"),
    path("edit-profile/", views.UserEditView.as_view(), name="edit-profile"),
    # path("password/", auth_views.PasswordChangeView.as_view())
    path("success/", views.PasswordChangeSuccessView, name="change-success"),
]
