from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register", views.CreateUserView.as_view(), name="register"),
    path("edit-profile/", views.UserEditView.as_view(), name="edit-profile"),
    # path("password/", auth_views.PasswordChangeView.as_view())
    path("success/", views.PasswordChangeSuccessView, name="change-success"),
    path("<int:pk>/profile/", views.ShowProfilePageView.as_view(), name="user-profile"),
    path("<int:pk>/edit-public-profile/", views.EditProfilePageView.as_view(), name="edit-public-profile"),
    #TODO: add the url
    path("<int:pk>/create-public-profile/", views.CreateProfilePageView.as_view(), name="create-public-profile")
]
