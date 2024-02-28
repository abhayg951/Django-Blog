from django.db.models.base import Model as Model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .form import CustomSignUpForm, CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.

class CreateUserView(generic.CreateView):
    form_class = CustomSignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class ChangePasswordView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('change-success')

def PasswordChangeSuccessView(request):
    return render(request, 'registration/change_password_success.html')