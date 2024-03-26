from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from .form import CustomSignUpForm, CustomUserChangeForm, CustomPasswordChangeForm, EditPublicProfileForm
from django.contrib.auth.views import PasswordChangeView
from . import models
from core.models import BlogPost
# from django.contrib.auth.

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

class ShowProfilePageView(generic.DetailView):
    model = models.UserProfile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self,  **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)

        page_user = get_object_or_404(models.UserProfile, id=self.kwargs['pk'])

        users_blogs = BlogPost.objects.filter(author_id = page_user.user.pk)
        # print(page_user.user.pk)
        # print(models.UserProfile.user.get_queryset())
        print(users_blogs)
        context["page_user"] = page_user
        context["page_user_blogs"] = users_blogs
        return context

class EditProfilePageView(generic.UpdateView):
    model = models.UserProfile
    template_name = 'registration/edit_public_profile_page.html'
    form_class = EditPublicProfileForm

class CreateProfilePageView(generic.CreateView):
    model = models.UserProfile
    template_name = 'registration/create_public_profile.html'
    form_class = EditPublicProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    